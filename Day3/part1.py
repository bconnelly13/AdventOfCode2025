def main():
    with open("input.txt") as f:
        banks = f.readlines()
    
    sum = 0
    for bank in banks:
        max_index = 0
        max_val = -1
        for i in range(len(bank)-2):
            if int(bank[i]) > max_val:
                max_val = int(bank[i])
                max_index = i
        next_best_index = max_index + 1
        next_best_val = int(bank[next_best_index])
        for j in range(max_index + 1, len(bank)-1):
            if int(bank[j]) > next_best_val:
                next_best_val = int(bank[j])
                next_best_index = j
        sum += max_val * 10 + next_best_val
    
    print("Total: ", sum)

main()