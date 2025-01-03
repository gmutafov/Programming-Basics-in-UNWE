some_str = input().lower()

vowels = [ 'a', 'e', 'i', 'o', 'u']

for char in some_str:
    if char in vowels:
        print('vowel')
    elif char.isdigit():
        print('number')
    else:
        print('other')