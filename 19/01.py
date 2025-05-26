def matrix(n=1,m=None, a=0):
    if not m:
        m = n
    return [[a for i in range(m)] for i in range(n)]

rows = matrix()
for row in rows:
    print(*row)