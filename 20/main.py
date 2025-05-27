# def print_boxed(arr):
#     arr_stringified = [str(element) for element in arr]
#     mid = ' | '.join(arr_stringified)
#     bar = '-' * (2 + len(mid))
#     print(' ' + bar + ' ')
#     print('| ' + mid + ' |')
#     print(' ' + bar + ' ')
#
#
# def print_simple(arr):
#     arr_stringified = [str(element) for element in arr]
#     print(', '.join(arr_stringified))
#
#
# formatting = 'boxed'
# if formatting == 'boxed':
#     print_formatted = print_boxed
# else:
#     print_formatted = print_simple
#
# # Дальше в программе можно использовать print_formatted повсюду
# print_formatted([1,1,2,3,5,8,13,21])
# print_formatted([1,2,4,8,16,32,64,128])
# print_formatted(['abc', 'def', 'ghi'])

# def is_word_long(word):
#     return len(word) >= 6
#
#
# words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные',
#     'слова']
# for word in filter(is_word_long, words):
#     print(word)

# Комбинированные функции
#  text = input().split()
#  numbers = map(lambda x: int(x) )

ENGLISH_ALPHABET = set([chr(c) for c in range(ord('a'),
    ord('z') + 1)])
RUSSIAN_ALPHABET = set([chr(c) for c in range(ord('а'),
    ord('я') + 1)] + ['ё'])
ALPHABET = ENGLISH_ALPHABET ^ RUSSIAN_ALPHABET

ENGLISH_VOWELS = {'a', 'e', 'i', 'o', 'u'}
RUSSIAN_VOWELS = {'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я'}
VOWELS = ENGLISH_VOWELS ^ RUSSIAN_VOWELS

def remove_punctuation(text: str) -> str:
    return ''.join(filter(lambda char: char.lower() in ALPHABET ^ {' '}, text))

def get_words(text):
    return remove_punctuation(text).split()

def number_of_vowels(word):
    return len(list(filter(lambda c: c in VOWELS, word)))

def long_words(text):
    return filter(lambda word: number_of_vowels(word) >= 4,
        get_words(text))

def print_long_words(text):
    for word in long_words(text):
        print(word.lower())