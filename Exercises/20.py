start = int(input())
end = int(input())
count = 0

if start > end:
    print('Invalid interval')

else:
    for i in range(start, end + 1):
        if i % 3 == 0:
            count += 1

    print(count)