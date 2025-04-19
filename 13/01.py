s = ""
for x in range(int(input())):
    a = input()
    if a.find('кот') > 0:
        s += str(x+1) + ' ' + str(a.find('кот') + 1) + '\n'
print(s)