# Строки. Индексация

text = 'Привет'

# Уникальность: возможны дубликаты
# Порядок: упорядоченная
# Изменяемость: неизменяемость
# Типы данных: односимвольные строки

# for char in text:
#     print(char, end=' ')
# for i in range(len(text)):
#     char = text[i]
#     print(char)
# for i, char in enumerate(text): Перебор элементов строки
#     print(i, char)
    # print(i + 1, ']', text[i], sep= ' ')

# print(text)
# text[2] = 'и'
# print(text)
# Индексация в строках

# 0 1 2 3 4 5
# П Р И В Е Т
# -6 -5 -4 -3 -2 -1 отрицательные индексы
# [0..n -1]
# [-1 .. -n]
# print(len(text))
# print(text[0])
# print(len(text) - 2)
# print(text[-2])

# a = 'война'
# b = 'мир'
#
# print(b > a)

# print(ord('A')) # получение соответветвующий ему символ в ASII
# print(chr(65)) # зная код можно получить соответствующий ему символ
# print(chr(48))
# print(chr(32))
# print(chr(67))

# print('\u2603')
# print('\U0001F6D5')

# Функция ord и chr
# for i in range(32):
#     print(chr(ord('А') + i), end=' ')

#  Функция chr
# print(ord('А'))
# print(ord('Б'))
# print(ord('В'))
# print(ord('Г'))



