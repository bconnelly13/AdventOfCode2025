with open("input.txt") as f:
    lines = f.readlines()

beamPoints = set()
for i in range(len(lines[0])):
    if lines[0][i] == 'S':
        beamPoints.add(i)

total = 0
for i in range(1, len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^' and j in beamPoints:
            total += 1
            if j != 0:
                beamPoints.add(j-1)
            if j != len(lines[i]) - 1:
                beamPoints.add(j+1)
            beamPoints.remove(j)

print(total)
            