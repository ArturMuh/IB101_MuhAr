# область видимости

# def print_array(array): # локальная
#     for element in array:
#         print(element)
#
#
# words = (['Hello', 'world']) # глобальная
# print_array(words)

# PI = 3.1415

# area = 'Красная площадь'
#
# def print_square_area(length, width):
#     area = length * width
#     print('Площадь площади: ', area)
#
# print('Место встречи: ', area)
# print_square_area(330, 75)
# print('Повторяю, место встречи: ', area)


ask_number = 0

def ask_again():
    global ask_number
    ask_number = ask_number + 1
    print('Ты спрашиваешь меня уже в ', ask_number, '-й раз', sep='')

ask_again()
ask_again()
ask_again()
print('---', ask_number)
