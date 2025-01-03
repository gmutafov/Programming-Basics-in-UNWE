number_of_words = int(input())

synonyms = {}

for _ in range(number_of_words):
    word = input()
    synonym = input()
    synonyms[word] = synonym

print(synonyms)
searched_word = input()

if searched_word in synonyms:
    print(synonyms[searched_word])

else:
    print('word not found')
