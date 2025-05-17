menu = []
receipt_counter = 1
def add_item(item_name: str, item_cost: int):
    menu.append((item_name, item_cost))


def print_receipt():
    global receipt_counter
    if not menu:
        return

    print(f'Чек {receipt_counter}. Всего предметов: {len(menu)}')
    for item_name, item_cost in menu:
        print(f'{item_name} - {item_cost}')
    print(f'Итого: {sum([cost for _, cost in menu])}')
    print('-----')

    receipt_counter += 1
    menu.clear()


add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()