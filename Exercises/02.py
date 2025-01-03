number_of_words = int(input())

synonyms = {}

for _ in range(number_of_words):
    word = input()
    synonym = input()
    synonyms[word] = synonym


searched_word = input()

if searched_word in synonyms:
    print(synonyms[searched_word])
    new_synonym = input()
    synonyms[searched_word] = new_synonym
    print(new_synonym)
else:
    print('word not found')

print(synonyms)