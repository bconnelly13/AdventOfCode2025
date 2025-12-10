def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    paper = "@"
    count = 0
    for line_num in range(len(lines)):
        line = lines[line_num]
        for column_num in range(len(line)):
            item = line[column_num]
            if item == paper:
                roll_count = 0
                row_above = (line_num != 0)
                row_below = (line_num != len(lines) - 1)
                col_left = (column_num != 0)
                col_right = (column_num != len(line) - 1)

                if col_left:
                    roll_count += (lines[line_num][column_num - 1] == paper)
                if col_right:
                    roll_count += (lines[line_num][column_num + 1] == paper)

                if row_above:
                    roll_count += (lines[line_num - 1][column_num] == paper)
                    if col_left:
                        roll_count += (lines[line_num - 1][column_num - 1] == paper)
                    if col_right:
                        roll_count += (lines[line_num - 1][column_num + 1] == paper)

                if row_below:
                    roll_count += (lines[line_num + 1][column_num] == paper)
                    if col_left:
                        roll_count += (lines[line_num + 1][column_num - 1] == paper)
                    if col_right:
                        roll_count += (lines[line_num + 1][column_num + 1] == paper)
                

                if roll_count < 4:
                    count += 1

    print("Total:", count)

main()