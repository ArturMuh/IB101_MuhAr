# Методы split join списочные выражения
ip = '192.168.0.1'
parts = ip.split('.') # разделенные части символы
print(parts)
parts[2] = '1'
print(parts)
ip = '.'.join(parts) # склеивание символов
print(parts)

# Списочные выражение
# squares = []
# for i in range(1, 11):
#     squares.append(i ** 2)
#
# print(squares)
# squares = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         squares.append(i ** 2)
#
# print(squares)
#
# squares = [i ** 2 for i in range(1, 11) if i % 2]
# print(squares)
#
# print([i * j for i in range(3) for j in range(3)])
# Считывание значений, введенных одной строкой
a = [int(x) for x in '976 929 289 809 7677'.split()]
evil, good = [int(x) for x in '666 777'.split()]
print(evil, good, sep='\n')

print(', '.join(str(i) + '^2=' + str(i ** 2) for i in range(1, 11)))
