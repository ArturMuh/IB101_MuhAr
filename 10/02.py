n = int(input())
data = []
for i in range(n):
	data.append(input())
search = input()
for text in data:
	if search in text:
	print(text)