n = int(input())
list = []
for i in range(n):
    list.append(input())
a = int(input())
list1 = []
for i in range(a):
    num = int(input())
    list1.append(list[num - 1])
print(list1)
