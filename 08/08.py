chislo =int(input())
while str(chislo)[0] != "1" and chislo < 1000000000:
   chislo *= int(str(chislo)[0])
print(chislo)