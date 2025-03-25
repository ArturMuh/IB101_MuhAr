Borya = int(input("Введите рост Бори: "))
Vova = int(input("Введите рост Вовы: "))
Dima = int(input("Введите рост Димы: "))

if Borya > Vova and Borya > Dima:
    if Vova > Dima:
        print(Borya, Vova, Dima)
    else:
        print(Borya, Vova, Dima)
elif Vova > Borya and Vova > Dima:
    if Borya > Dima:
        print(Borya, Vova, Dima)
    else:
        print(Borya, Vova, Dima)
elif Dima > Borya and Dima > Vova:
    if Borya > Vova:
        print(Borya, Vova, Dima)
    else:
        print(Borya, Vova, Dima)
