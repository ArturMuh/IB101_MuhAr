last_message = ''

def print_without_duplicates(message:str):
    global last_message
    if last_message == message:
        return
    print(message)
    last_message = message


print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Когда доедешь до дома")
print_without_duplicates("Ага, жду")
print_without_duplicates("Ага, жду")