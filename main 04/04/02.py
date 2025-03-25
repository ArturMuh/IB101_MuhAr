parol1 = input("Введите пароль:")
dl_parol1 = len(parol1)
parol2 = input("Повторите пароль:")
dl_parol2 = len(parol2)
while dl_parol1 < 8:
    print('Короткий')
    break
while dl_parol1 > 8 and parol1 == parol2:
    print('OK')
    break
while parol1 != parol2:
    print('Различаются')
    break
