def get_email(name, date, email, gorod='Нефтекамск'):
    return f"""To: {email} Здравствуйте, {name}! Были бы рады видеть вас на встрече начинающих программистов в {gorod}, которая пройдет {date}."""

email1 = get_email(
    name="Рустам",
    date="27.05.2025",
    email="Axhemetov03@mail.ru",
    gorod="Нефтекамск"
)

email2 = get_email(
    name="Ильназ",
    date="27.05.2025",
    email="Ilnaz@gmail.com"
)

print(email1)
print("\n" + "--" * 10 + "\n")
print(email2)