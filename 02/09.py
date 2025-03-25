login = input("Enter your login: ")
email = input("Enter your email: ")
if "@" in login:
    print("Некорректный логин")
elif "@" not in email:
    print("Некорректный адрес")
else:
    print("ОК")