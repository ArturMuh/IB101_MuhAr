count = 0
prenum = 0
for i in range(16):
    num = int(input())
    if prenum % num == 0:
        print('ДА')
    else:
        print('НЕТ')
        prenum = num