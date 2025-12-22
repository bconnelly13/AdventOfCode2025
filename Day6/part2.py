
with open("input.txt") as f:
    lines = f.readlines()

problemLines = lines[:len(lines) - 1]
symbols = [symbol for symbol in lines[len(lines) - 1].strip().split(" ") if symbol != '']

lastColUsed = -1
problems = []
for i in range(len(problemLines[0])):
    allEmpty = True
    for line in problemLines:
        if line[i] != ' ':
            allEmpty = False
            break
    if allEmpty:
        newProblem = []
        for line in problemLines:
            newProblem.append(line[lastColUsed+1:i])
        problems.append(newProblem)
        lastColUsed = i

newProblem = []
for line in problemLines:
    newProblem.append(line[lastColUsed+1:i])
problems.append(newProblem)

finalProblems = []
for problem in problems:
    newIntProblem = []
    numLength = len(problem[0])
    for i in range(numLength):
        strNum = ''
        for num in problem:
            strNum += num[numLength - i - 1]
        newIntProblem.append(int(strNum.strip()))
    finalProblems.append(newIntProblem)

total = 0
for i in range(len(symbols)):
    symbol = symbols[i]
    if symbol == '+':
        total += sum(finalProblems[i])
    elif symbol == '*':
        prod = 1
        for num in finalProblems[i]:
            prod *= num
        total += prod

print(total)
