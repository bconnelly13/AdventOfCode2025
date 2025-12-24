import math

def main():
    with open("input.txt") as f:
        lines = f.readlines()


    dists = {}
    points = []
    for line in lines:
        coords = line.split(",")
        intCoords = []
        for coord in coords:
            intCoords.append(int(coord))
        points.append(intCoords)

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dists[(i,j)] = findDist(points[i], points[j])

    sorted_dists = dict(sorted(dists.items(), key=lambda item: item[1]))

    circuits = [i for i in range(len(points))]
    counts = [1 for _ in range(len(points))]

    result = -1
    for key in sorted_dists:
        pointARoot = findRoot(circuits, key[0])
        pointBRoot = findRoot(circuits, key[1])
        if pointARoot != pointBRoot:
            circuits[pointBRoot] = pointARoot
            counts[pointARoot] += counts[pointBRoot]
        if counts[pointARoot] == len(points):
            result = points[key[0]][0] * points[key[1]][0]
            break
            
    print("Result:", result)



def findDist(pointA, pointB):
    return math.sqrt(sum((pointA[i] - pointB[i]) ** 2 for i in range(len(pointA))))

def findRoot(circuits, node):
    if circuits[node] != node:
        circuits[node] = findRoot(circuits, circuits[node])
    return circuits[node]

main()