N = int(input())
names = [input()
    for i in range(N)]
n = int(input())
K = int(input())
for j in range(K):
    del names[n - 1::n]
print('\n'.join(names))