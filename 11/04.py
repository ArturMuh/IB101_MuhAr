N = []
kol_strok = int(input())
for i in range(kol_strok):
    N.append(input())
for i in range(kol_strok):
    for j in range(i+1,kol_strok):
        if len(N[i]) > len(N[j]):
            N[i], N[j] = N[j], N[i]
        if len(N[i]) == len(N[j]):
            N[i], N[j] = N[j], N[i]
print(*N, sep="\n")