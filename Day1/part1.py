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
        spot %= 100
        if spot == 0:
            count += 1
    print(f"Count: {count}")

main()
 