N = int(input())
n = []
bez_puncta= []
for i in range(N):
    n.append(input())
for i in n:
    if "лук" not in i:
        bez_puncta.append(i)
print(", ".join(bez_puncta))