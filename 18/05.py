def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)

arr = [1, 2]
mirror(arr)
print(*arr)