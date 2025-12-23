with open("input.txt") as f:
    lines = f.readlines()



rows = len(lines)
cols = len(lines[0])
paths = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(len(lines[0])):
    if lines[0][i] == 'S':
        paths[0][i] = 1

for i in range(1, len(lines)):
    for j in range(len(lines[i])):
        pathSpots = 0
        if lines[i-1][j] != '^':
            pathSpots += paths[i-1][j]
        if j != 0 and lines[i-1][j-1] == '^':
            pathSpots += paths[i-1][j-1]
        if j != len(lines[i]) - 1 and lines[i-1][j+1] == '^':
            pathSpots += paths[i-1][j+1]
        paths[i][j] = pathSpots
    
sum = 0
for i in range(len(lines[-1])):
    sum += paths[-1][i]

print(sum)





