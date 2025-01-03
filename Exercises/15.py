price = float(input())
discount = int(input()) / 100

if price < 0:
    print('Invalid price')
elif discount < 0:
    print('Invalid discount')
else:

    print(price - (price * discount))