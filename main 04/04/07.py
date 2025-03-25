begin = 1
end = 1000
finished = False
attemtps = 1000000
prev = -1
while not finished and attemtps > 0:
    guess = (end + begin) // 2
    if guess == prev:
        if guess < end:
            guess = begin
        else:
            guess = end
    prev = guess
    answer = input(str(guess) + '? ')
    if answer == '=':
        finished = True
    elif answer == '>':
        begin = guess
        attemtps -= 1
    elif answer == '<':
        end = guess
        attemtps = -1

    # num = begin / end // 2
    # print(num)
    # text = input("Введите >, < или =")
