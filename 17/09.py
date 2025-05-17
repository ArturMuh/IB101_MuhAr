base = ['Иван', 'Юлия Иванкова']

def hello(name: str):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')

def search_card(name: str):
    if name in base:
        card_number = base.index(name) + 1
        print(f'Ваша карта с номером {card_number} найдена')
    else:
        print('Ваша карта не найдена')

base = ['Иван', 'Юлия Иванкова']

hello('Иван')
search_card('Иван')
hello('Юлия Иванова')
search_card('Юлия Иванова')