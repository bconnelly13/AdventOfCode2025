def main():
    ranges = []
    ids = []
    with open("input.txt") as f:
        line = f.readline().strip()
        while line != "":
            ranges.append(tuple(int(x) for x in line.split("-")))
            line = f.readline().strip()
        line = f.readline().strip()
        while line and line != "":
            ids.append(int(line))
            line = f.readline().strip()

    ranges.sort()
    count = 0
    for id in ids:
        for r in ranges:
            if r[0] > id:
                break
            if r[1] >= id:
                count += 1
                break

    print("Total:", count)

main()