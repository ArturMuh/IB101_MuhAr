city1 = input()
while True:
    city2 = input()
    if city1[-1] != city2[0]:
        print(city2)
        break
    city1 = city2
