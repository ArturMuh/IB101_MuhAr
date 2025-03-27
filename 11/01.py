n = int(input())
data = []
answer = 'False'
for i in range(n):
    data.append(int(input()))
k = int(input())
for i in range(n):
    if answer:
        break
    for j in range(i + 1, n):
        if data[i] * data[j] == k:
            answer
    print('Да')
else:
    print('Нет')