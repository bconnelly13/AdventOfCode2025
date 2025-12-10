def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    spot = 50
    count = 0
    for line in lines:
        direction = line[0]
        number = int(line[1:])
        if direction == "L":
            spot -= number
        elif direction == "R":
            spot += number
        else:
            print("INVALID DIRECTION {direction}")
        tmp = 0
        while (spot >= 100):
            spot -= 100
            tmp += 1
        while (spot < 0):
            spot += 100
            tmp += 1
        count += tmp
    print(f"Count: {count}")

main()
 