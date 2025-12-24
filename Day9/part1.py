def main():
    with open("input.txt") as f:
        lines = f.readlines()

    points = []
    for line in lines:
        coords = line.split(",")
        intCoords = []
        for coord in coords:
            intCoords.append(int(coord))
        points.append(intCoords)

    max_area = -1
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            area = findArea(points[i], points[j])
            if area > max_area:
                max_area = area
    
    print("Max Area:", max_area)

def findArea(point1, point2):
    return abs(point1[0] - point2[0] + 1) * abs(point1[1] - point2[1] + 1)

main()

