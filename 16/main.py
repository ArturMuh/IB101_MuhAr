# text = input()
# def double_it(x): # возвращение значения
#     return x * 2 # удваивает значение
#
# def round_square(r):
#     return 3.14 * r ** 2
#
# def round_length(r):
#     return  double_it(3.14 * r)
#
#
# a = double_it(3)
# b = double_it(5)

# def my_abs(x: int | float): # множественные точки возврата из фунции
#     if x >= 0:
#         result = x
#     else:
#         result = -x
#
# print(my_abs(4))
# print(my_abs(-4))

# def my_abs(x):
#     if x >= 0:
#         return x
#     return -x

# def matrix_has_close_value(
#         matrix:list[list],
#         value:int | float,
#         eps: int | float):
#     found = False
#     for row in matrix:
#         for el in row:
#             if abs(el - value) <= eps:
#                 if abs(el - value) <= eps:
#                     return True
#                     return False


def get_coordinates(): #Возврат нескольких значений
    x = 1
    y = 2
    return x, y

print(get_coordinates())

def get_coordinates(index):
    if index == 2:
        return 1.5, 2.5
    else:
        return 1.5, 2.5, 0