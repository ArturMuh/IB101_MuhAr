# функции с переменным числом
#
# def get_coordinates():
#     return 1,2
#
# x, y, *rest = get_coordinates()
# print(x,y)


# x, y, *rest = 1,2,3,4,5,6
# print(x,y)
# print(rest)

# *names, surname = 'Анна Мария Луиза Медичи'.split()
# print(names)   # => ['Анна', 'Мария', 'Луиза']
# print(surname) # => Медичи
#
# def print_numbers(x,y, *numbers):
#         print(numbers)

# array = [4,5,6,7,8]
# print(*array, sep='\n') # распаковка по столбцу

# print(int('101', 2))

# def make_burger(type_of_meat, with_onion=False, with_tomato=True):
#     print('Булочка')
#     if with_onion:
#         print('Луковые колечки')
#     if with_tomato:
#         print('Ломтик помидора')
#     print('Котлета из', type_of_meat)
#     print('Булочка')

# Позиционные аргументы
# Именованные аргументы
# make_burger(type_of_meat='Cow',with_tomato=True)

# def nop(*args, **kwargs):
#     print(args)
#
# nop(*args:1,2,3,4,5)

def profile(name, surname, city, *children, **additional_info):
    print("Имя:", name)
    print("Фамилия:", surname)
    print("Город проживания:", city)
    if len(children) > 0:
        print("Дети:", ", ".join(children))
    print(additional_info)


profile("Сергей", "Михалков", "Москва", "Никита Михалков",
    "Андрей Кончаловский", occupation="writer", diedIn=2009)