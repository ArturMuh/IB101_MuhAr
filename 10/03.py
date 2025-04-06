n = int(input())
data = []
answer = ''
for i in range(n):
	data.append(input())
pos = int(input())
for text in data:
	if len(text) >= pos:
		answer += text[pos - 1]
print(answer)