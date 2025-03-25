num_home1 = set()
num_home2 = set()
count = 0
a = input()
while count < 2:
    a = input()
    if not a:
        count += 1
        continue
    if count == 0:
            num_home1.add()
    b = input()
    while b:
        num_home2.add(b)
        b = input()
    num_home3 = num_home1 & num_home2
    if not num_home3:
        print('EMPTY')
    else:
        print(num_home3)
