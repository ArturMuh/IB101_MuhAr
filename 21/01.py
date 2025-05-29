words = input().split()
sorted = sorted(words, key=lambda x: x.lower())
print(' '.join(sorted))


