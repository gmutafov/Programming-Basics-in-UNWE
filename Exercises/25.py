n = int(input())
nums = [input() for _ in range(n)]

powered_nums = sorted([int(i) ** 2 for i in nums])
[print(num) for num in powered_nums]