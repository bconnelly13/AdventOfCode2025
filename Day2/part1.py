def main():
    with open("input.txt") as f:
        input = f.readline()

    tmp = input.split(",")
    ranges = []
    for inputRange in tmp:
        a, b = inputRange.split("-")
        ranges.append((int(a), int(b)))
    
    sum = 0
    for interval in ranges:
        for i in range(interval[0], interval[1] + 1):
            strNum = str(i)
            if len(strNum) % 2 == 0:
                firstHalf = strNum[:len(strNum)//2]
                secondHalf = strNum[len(strNum)//2:]
                if (firstHalf == secondHalf):
                    sum += i
    
    print(f"Total: {sum}")

main()