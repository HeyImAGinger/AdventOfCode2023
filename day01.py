
with open('/Users/etiennemiltgen/Developpement/AdventOfCode2023/day01.txt', 'r') as file:
    total_sum = 0
    for line in file:
        line = line.strip()
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = char
                    last_digit = char
                else:
                    last_digit = char
        digit_sum = first_digit + last_digit
        total_sum += int(digit_sum)
        print(digit_sum)
    print("Total sum:", total_sum)
