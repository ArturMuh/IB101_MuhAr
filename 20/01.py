def arithmetic_operation(operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return operations.get(operation, lambda x, y: None)

operation = arithmetic_operation('+')
assert (operation(1, 4))
operation = arithmetic_operation('-')
assert (operation(1, 4))
operation = arithmetic_operation('*')
assert (operation(1, 4))
operation = arithmetic_operation('/')
assert (operation(1, 4))