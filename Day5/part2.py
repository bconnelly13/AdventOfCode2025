def main():
    ranges = []
    with open("testinput.txt") as f:
        line = f.readline().strip()
        while line != "":
            ranges.append(tuple(int(x) for x in line.split("-")))
            line = f.readline().strip()

    ranges.sort()
    count = 0
    max_considered = -1
    for r in ranges:
        start = max(r[0], max_considered + 1)
        if r[1] >= start:
            count += r[1] - start + 1
            max_considered = r[1]
        
    print("Total:", count)

main()