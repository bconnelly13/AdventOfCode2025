import pulp

def solve_machine(A, b):
    n = len(b)
    m = len(A)

    prob = pulp.LpProblem("joltage", pulp.LpMinimize)
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(m)]
    prob += sum(x)

    for i in range(n):
        prob += sum(x[j] for j in range(m) if i in A[j]) == b[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    return [vj.value() for vj in x], pulp.value(prob.objective)


with open("input.txt") as f:
    lines = f.readlines()

# Preprocess input
allJoltages = []
allButtons = []
for line in lines:
    line = line.strip("\n")
    endOfLights = line.index("]")
    startOfJoltages = line.index("{")
    lineJoltageStr = line[startOfJoltages+1:len(line)-1]

    buttonsString = line[endOfLights+1:startOfJoltages].strip()
    lineButtons = [lineButton.strip("()") for lineButton in buttonsString.split(" ")]
    
    lineJoltages = [int(num) for num in lineJoltageStr.split(",")]
    allJoltages.append(lineJoltages)

    machineButtons = []
    for button in lineButtons:
        buttonNums = [int(num) for num in button.split(",")]
        machineButtons.append(buttonNums)
    allButtons.append(machineButtons)

total = 0
for i in range(len(allJoltages)):
    joltages = allJoltages[i]
    buttons = allButtons[i]

    solution, numPresses = solve_machine(buttons, joltages)
    total += numPresses

print("Total", total)
