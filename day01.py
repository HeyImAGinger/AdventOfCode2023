
with open('/Users/etiennemiltgen/Developpement/AdventOfCode2023/day01.txt', 'r') as file:
    total_sum = 0
    for line in file:
        line = line.strip()
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = int(char)
                    last_digit = int(char)
                else:
                    last_digit = int(char)
        digit_sum = str(first_digit) + str(last_digit) if last_digit is not None else str(first_digit)
        total_sum += int(digit_sum)
        print(digit_sum)
    print("Total sum:", total_sum)
