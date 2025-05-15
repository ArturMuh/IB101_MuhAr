def number_to_words(n):
    units =["", "один", "два", "три", "четыре", "пять", "шесть", "семь","восемь", "девять"]
    teens = ["десять","одиннадцать", "двенадцать","тринадцать", "четырнадцать",
             "пятнадцать", "шестнадцать","семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["","десять","двадцать","тридцать","сорок","пятьдесять",
            "шестьдесять","семьдесять", "восемьдесять", "девяносто"]
    hundreds = ["", "сто", "двести", "тристо", "четыресто", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if 10 <= n <= 19:
        return teens[n - 10]
    if n >= 20:
        hundreds_part = hundreds[n // 100]
        n = n % 100
        ten_part = tens[n // 10]
        unit_part = units[n % 10]
        return (hundreds_part + ' ' + ten_part + ' ' + unit_part).strip()

    return units[n]

print(number_to_words(4))
print(number_to_words(14))
print(number_to_words(34))
print(number_to_words(104))
print(number_to_words(114))
print(number_to_words(124))


