a = input("Введите сообщение:")
user = int(len(a) * 40)
kop = user % 100
sum = user // 100
rubl = user
print(rubl, 'р.', kop, 'коп.')