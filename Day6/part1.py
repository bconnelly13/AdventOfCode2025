
with open("input.txt") as f:
    lines = f.readlines()

problems = []
symbols = []

for i in range(len(lines)):
    line = lines[i]
    if i == len(lines) - 1:
        symbols = [symbol for symbol in line.strip().split(" ") if symbol != '']
    else:
        nums = [num for num in line.strip().split(" ") if num != '']
        for j in range(len(nums)):
            if len(problems) <= j:
                problems.append([])
            problems[j].append(int(nums[j]))
    

total = 0
for i in range(len(symbols)):
    symbol = symbols[i]
    if symbol == '+':
        total += sum(problems[i])
    elif symbol == '*':
        prod = 1
        for num in problems[i]:
            prod *= num
        total += prod

print(total)