chislo = int(input("Введите количество символов: "))
pervoe_chislo = 0
for i in range(chislo):
    a = int(input("Введите число: "))
    if i % 2 == 0:
        pervoe_chislo += a
    else:
        pervoe_chislo -= a
print(pervoe_chislo)