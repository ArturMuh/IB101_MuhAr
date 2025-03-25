s = int(input())
founded = False
for i in range(s):
    text = input()
    if ("кот" or "Кот") in text:
        founded = True
        if ("Пес" or "пес") in text:
            founded = False
if founded == True:
    print("МЯУ")
else:
    print("НЕТ")