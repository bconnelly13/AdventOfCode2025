def main():
    with open("input.txt") as f:
        input = f.readline()

    tmp = input.split(",")
    ranges = []
    for inputRange in tmp:
        a, b = inputRange.split("-")
        ranges.append((int(a), int(b)))
    
    sum = 0
    ids = []
    for interval in ranges:
        for id in range(interval[0], interval[1] + 1):
            strNum = str(id)
            for idLen in range(1, (len(strNum) // 2) + 1):
                if len(strNum) % idLen == 0:
                    splitNum = []
                    for i in range(len(strNum) // idLen):
                        splitNum.append(strNum[i*idLen:(i+1)*idLen])
                    if (len(set(splitNum)) == 1):
                        sum += id
                        break
    
    print(f"Total: {sum}")

main()