kol_sotrud = int(input())
familiya = set()
familiya2 = set()
odinakoc_name =0
for i in range(kol_sotrud):
    name = input()
    if not name in familiya:
        familiya.add(name)
        familiya2.add(name)
    elif name in familiya2:
        odinakoc_name += 2
        familiya2.discard(name)
    else:
        odinakoc_name += 1
print(odinakoc_name)