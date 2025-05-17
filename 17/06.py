translated_text = None
def translate(text):
    global translated_text
    translatedText = ''
    redLetter = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                 '.', ',', '-', '!', '?', ';', ' ', '(', ')', '"']
    for char in text:
        if char not in redLetter:
            translatedText += char
    translated_text = ' '.join(translatedText.split())
translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")
print(translated_text)

