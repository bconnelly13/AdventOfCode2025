def main():
    with open("input.txt") as f:
        banks = [line.strip() for line in f.readlines()]

    sum = 0
    for bank in banks:
        max_num = []
        indices = []
        num_len = 12
        for i in range(num_len):
            max_index = -1
            max_val = -1
            prev_index = indices[i-1] if i > 0 else -1
            for i in range(prev_index + 1, len(bank)-(num_len - 1 - i)):
                if int(bank[i]) > max_val:
                    max_val = int(bank[i])
                    max_index = i
            max_num.append(max_val)
            indices.append(max_index)
        
        sum += int(''.join(str(val) for val in max_num))
    
    print("Total: ", sum)

main()