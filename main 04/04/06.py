is_correct = True
while is_correct:
    password = input()
    confirm = input()
    if len(password) < 8:
        print('Короткий')
    elif '123' in password:
        print('Простой')
    elif password != confirm:
        print('Различаются')
    else:
        is_correct = True
print('OK')


