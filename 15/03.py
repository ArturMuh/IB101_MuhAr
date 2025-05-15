def quarter(xcord:float, ycord: float):
    if xcord > 0 and ycord > 0:
        print('I четверть')
    elif xcord < 0 and ycord > 0:
        print('II четверть')
    elif xcord < 0 and ycord < 0:
        print('III четверть')
    else:
        print('IV четверть')

quarter(1,1)
quarter(-2,5)
quarter(-8.5,-5)
quarter(2,-6)