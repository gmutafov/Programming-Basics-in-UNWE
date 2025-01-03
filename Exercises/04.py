n = int(input("How many numbers: "))

for _ in range(n):
    number = int(input())

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")