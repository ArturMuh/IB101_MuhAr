num = int(input())
founded = False
for i in range(num - 1):
    text = input()
    if ("кот" or "Кот") in text:
        text = input()
        founded = True
    if founded == True:
        print('МЯУ')
    else:
        print('НЕТ')

