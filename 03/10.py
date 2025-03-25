num1 = float(input("Введите число: "))
num2 = float(input("Введите число: "))
operator = input("Введите действие: ")
if operator == "+":
   print(num1 + num2)
elif operator == "-":
   print(num1 - num2)
elif operator == "*":
   print(num1 * num2)
elif operator == "/":
   if num2 != 0:
       print(num1 / num2)
   else:
       print(888888)
else:
   print(888888)