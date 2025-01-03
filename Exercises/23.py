a = float(input())
b = float(input())
c = float(input())

if a <= 0 or b <= 0 or c <= 0:
    print('Invalid input')

else:
    print(f"P={a + b + c}")
    print(f"S={(a * b) / 2}")