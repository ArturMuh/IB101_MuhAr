n = int(input())
founded = False
for i in range(n):
    text = input()
    if ("кот" or "Кот") in text:
        founded = True
        break
        text = input()
    if founded == True:
        print('МЯУ')
    else:
        print('НЕТ')

