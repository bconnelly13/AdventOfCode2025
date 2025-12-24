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

    # print(points)
    point1 = None
    point2 = None
    max_area = -1
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            area = findArea(points[i], points[j])
            # print(points[i], points[j], area)
            if area > max_area:
                max_area = area
                point1 = points[i]
                point2 = points[j]
    
    print("Max Area:", max_area)

def findArea(point1, point2):
    return abs(point1[0] - point2[0] + 1) * abs(point1[1] - point2[1] + 1)

main()

