list_of_numbers = input().split(',')
count = 0
max_number = max(list_of_numbers)

for number in list_of_numbers:
    if number == max_number:
        count += 1

print(max_number)
print(count)