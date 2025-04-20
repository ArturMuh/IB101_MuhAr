stack = []
while True:
    text = input()

    if not text:
        print('...')
        continue
    founded = True
    for c in text:
        if c in '(<{':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                founded = False
                break
        elif c == '>':
            if not stack or stack.pop() != '<':
                founded = False
                break
        elif c == '}':
            if not stack or stack.pop() != '{':
                founded = False
                break

    if founded and not stack:
        print("Скобки валидны.")
    else:
        print("Скобки не валидны.")
