parol = list(input())
for i in parol:
    if i not in '1234567890_qwertyuiopasdfghjklzxcvbnm':
        print('Неверный символ:', i)
        break
else:
    print('OK')