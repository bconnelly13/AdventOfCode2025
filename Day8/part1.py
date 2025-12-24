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

    connections = 0
    MAX_CONNECTIONS = 1000
    for key in sorted_dists:
        pointARoot = findRoot(circuits, key[0])
        pointBRoot = findRoot(circuits, key[1])
        if pointARoot != pointBRoot:
            circuits[pointBRoot] = pointARoot
            
        connections+=1
        if connections == MAX_CONNECTIONS:
            break

    circuit_sizes = {}
    for circuit in circuits:
        root = findRoot(circuits, circuit)
        if root in circuit_sizes:
            circuit_sizes[root] += 1
        else:
            circuit_sizes[root] = 1

    sorted_circuit_counts = dict(sorted(circuit_sizes.items(), key=lambda item: item[1], reverse=True))

    count = 0
    total = 1
    for key in sorted_circuit_counts:
        count += 1
        total *= sorted_circuit_counts[key]
        if count == 3:
            break

def findDist(pointA, pointB):
    return math.sqrt(sum((pointA[i] - pointB[i]) ** 2 for i in range(len(pointA))))

def findRoot(circuits, node):
    if circuits[node] != node:
        circuits[node] = findRoot(circuits, circuits[node])
    return circuits[node]

main()