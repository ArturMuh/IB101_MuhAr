city1 = str(input("Введите 1 город"))
city2 = str(input("Введите 2 город"))
if city1 != city2 and (city1 == 'Тула' and city2 != 'Пенза' or city1 != 'Тула' and city2 == 'Пенза'):
    print('Да')
else:
    print('Нет')