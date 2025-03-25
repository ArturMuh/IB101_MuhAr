height = int(input("Количество строк:"))
for stage in range(1, height*2, 2):
    space = ' ' * (height - stage - 1)
    symbols = '*' * (stage * 2 + 1)
    print(space, symbols, space, sep='')

