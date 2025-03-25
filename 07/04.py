m = int(input())
n = int(input())
list0 = set()
count = 0
for _ in range(m+n):
    name = input()
    if name in list0:
        count += 1
    list0.add(name)
    print(len(list0) - count)
