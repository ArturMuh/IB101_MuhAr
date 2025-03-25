shag_shifr = int(input())
word = input()
for i in range(len(word)):
    f = ord(word[i])
    j = f + shag_shifr
    print(chr(j), end="")