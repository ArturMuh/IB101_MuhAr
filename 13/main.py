# Методы списков и строк

# a = set()
# print([x for x in dir(a) if not x.startswith('__')])
# print(help(input))
# a = [2,3,7]
# print(a.index(7))
#
# print(sum([2, 3, 7]))
# a = [2,3,7]
# a.remove(3)
# print(a)
# a = [3,2,7]
# a.sort()
# print(a)
# s = 'abracadabra'
# print(s.rfind('ab')) #индекс начала последнего вхождения подстроки
#
# s = 'abracadabra'
# print(s.startswith(s)) # Проверка, что s начинается с s2
# d = 12
# m = 4
# y = 2025
# print('.'.join([str(d).rjust(2,0), str(m).rjust(2, 0), str(y)]))
# Добавляет слева нужное количество символов c, чтобы длина s достигла k
# d = '4'.rjust(2, 0)
# m = '4'.rjust(2, 0)
# y = 2025
# print(d + '.' + m + '.' + str(y))
# print(f'{d}.{m},{y}')
# name = "Аркадий"
# age = 14
# print(f"Меня зовут {name} Мне {age} лет.")
# LIFO - стопка
array = []
for i in range(1,6):
    array.append(input(f'Put {i} t-shirt:'))
while array:
    print(array.pop())
# for el in array[::-1]:
#     print(el)
