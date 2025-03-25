n = int(input())
list1 = []
list2 = []
for i in range(n):
    line = int(input())
    list1.append(line)
    list2.append(line)
for i in range(n):
    list2[i] = list2[i] * 3
for i in range(n):
    print(list1[i])
    print()
for i in range(n):
    print(list2[i])