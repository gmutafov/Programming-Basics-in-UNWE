egn = input()

year = int(egn[:2])
month = int(egn[2:4])
day = int(egn[4:6])

if 1 <= month <= 12:
    year += 1900
elif 21 <= month <= 32:
    year += 1800
    month -= 20
elif 41 <= month <= 52:
    year += 2000
    month -= 40


age = 2019 - year

if age >= 18:
    print("adult")
else:
    print("juvenile")
