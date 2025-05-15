def find_mountain(heights_map: list[list[int]]):
    t = []
    for i in heights_map:
        t.append(max(i))
    s = max(t)
    for i in range(len(heights_map)):
        if s in heights_map[i]:
            row = i
    for i in heights_map:
        for j in range(len(i)):
            if s == i[j]:
                col = j
    return (row, col)