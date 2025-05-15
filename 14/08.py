spisok = {}
for i in range(int(input())):
    text = input().split()
    word = text
    spisok[word[0]] = text[len(word[0]) + 1:]

for k in range(int(input())):
    word = input()
    if word not in spisok:
        print('Нет в словаре')
    else:
        print(spisok[word])