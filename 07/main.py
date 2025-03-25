# Множества

# animals = {'cat','dog','fox', 'elephant'}
# # animals = set() значение элемента множества
# print(animals)
# animals.add('cow')
# print(animals)
# # animals.discard('dog') удалить заданный элемент
# print(animals)
# animals.remove('dog')
# print(animals)
# if 'dog' in animals:
#     animals.remove('dog') удалить
# print(animals)
# Порядок: неупорядоченная коллекция
# Изменяемость: Изменяемая коллекция - animals.add('cow')
# Типы данных: незименяемые типы
# Уникальность: уникальные
# animals = {'cat','dog','fox', 'elephant'}
# # animals = set() значение элемента множества
# print(animals)
# animals.add('cow')
# print(animals)
# # animals.discard('dog')
# print(animals)
# animals.remove('dog')
# print(animals)
# animals.pop() # удаляет некоторый элемент из множества
# print(animals)
# # clear - очисть множество
# print('cat' in animals)
# print('wolf' not in animals)
# print(len(animals))
# while animals:
#     animals = animals.pop()
#     print('->', animals)

# Объединение множества
# set_1 = {1,2,3,4}
# set_2 = {3,4,5,6}
# set_3 = set_1.union(set_2)
# print(set_2)

# set_1 = {1,2,3,4}
# set_2 = {3,4,5,6}
# set_union = set_1 | set_2 # Объединение
# print('Union:', set_union)
# set_intersection = set_1 & set_2 # Пересечение
# print('Intersection:',set_intersection)
# set_diff = set_1 - set_2 # Разность
# print('Differences:', set_diff)
# set_sym_diff = set_1 ^ set_2 # Симметричная разность
# print('Symetric diff', set_sym_diff)
# print((set_1 | set_2) - (set_1 & set_2))
# print((set_1 | set_2) | (set_1 & set_2))

set_1 = {4,5,3,6}
set_2 = {3,4,5,6}
set_3 = {3,4}
print(set_1 == set_2)
print(set_2 != set_3)
print(set_2 < set_3)
print(set_2 > set_3)
print(set_2 <= set_3)
print(set_2 <= set_3)
