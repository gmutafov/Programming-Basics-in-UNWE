some_str = input()

num_list = []

for char in some_str:
    if char.isdigit():
        num_list.append(char)

num_list.sort()
print('\n'.join(num_list))