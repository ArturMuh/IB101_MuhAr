en = set()
de = set()
m = int(input())
n = int(input())
for _ in range(m):
    en.add((input()))
for _ in range(n):
    de.add(input())
ende = en ^ de
print(len(ende))
