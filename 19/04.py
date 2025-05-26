def partial_sums(*args):
    temp = [0]
    for i in range(len(args)):
        temp.append(temp[i] + args[i])
    return temp

print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))