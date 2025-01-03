num = input()

sum_of_digits = sum(int(digit) for digit in num)
reversed_num = num[::-1]
last_to_first = num[-1] + num[:-1]
swapped_digits = num[0] + num[2] + num[1] + num[3]

print(sum_of_digits)
print(reversed_num)
print(last_to_first)
print(swapped_digits)