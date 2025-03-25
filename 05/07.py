num = int(input())
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=' ')
        count += 1
else:
    print()
if count > 0:
    print()
if count == 2:
    print('\n' 'ПРОСТОЕ')
else:
    print('\n' 'НЕТ')

