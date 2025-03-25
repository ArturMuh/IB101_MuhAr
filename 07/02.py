n = int(input())
cities = set()
for i in range(int(input())):
    cities.add(input())
new_city = input()
if new_city not in cities:
    print('OK')
else:
    print('TRY ANOTHER')
