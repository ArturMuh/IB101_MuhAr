def transpose(matrix: list[list[int]]):
    temp = matrix[:]
    matrix.clear()
    for i in range(len(temp)):
        matrix += [[j[i] for j in temp]]

matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)