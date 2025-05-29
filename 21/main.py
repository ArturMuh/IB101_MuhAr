# Обработка коллекций

# array = filter(lambda x: x % 3 == 0, range(100))
# print(array)

# result = sum([x ** 2 for  x in range(50 * 10 ** 8)]) # 19gb

# result = sum(map(lambda x: x ** 2, range(50 * 10 ** 8))) # 6mb

# words = ['мир', 'и', 'война']
# words = ['Собака', 'Кот', 'Морж','попугай','удав','аист']
# print(sorted(words, key=lambda s: -len(s))) # сортировка по убыванию
# key=lambda s: 1 if s[0].islower() else 0 # убываение длины
#
# li = [
#     ['Crawl', 'R', 61],
#     ['Stuber', 'R', 42],
#     ['Midsommar', 'R', 73],
#     ['Yesterday', 'PG-13', 56],
#     ['Annabelle Comes Home', 'R', 53],
#     ["Child's Play", 'R', 48],
#     ['Anna', 'R', 40],
#     ['Toy Story 4', 'G', 84],
#     ['Shaft', 'R', 40],
#     ['Men in Black: International', 'PG-13', 38]
# ]
# print(*sorted(li, key=lambda item: (item[1], -item[2], item[0])), sep='\n')

# key принимает max и min для сортировки

# проверка коллекции

# numbers = [1,2,3,4,5,6,7,8,9]
#
# print(all(numbers)) # ...
# print(all([]))
# print(all([1,3,'',123]))
# print()
# print(any(numbers)) # ...

words = "Ехал грека через реку".split()
print(any(map(lambda w: len(w) >= 5, words)))

# Потоковый ввод stdin

import  sys

for line in sys.stdin:
    print(line.rstrip('\n'))
print('-' * 10)
print('End')
# sys.stdin # интератор объект





