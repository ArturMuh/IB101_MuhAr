def number_in_english(number: int | str):
    chislo = {
        '': '',
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'ten',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninty',
    }
    if number in chislo:
        return chislo[number]

    if number < 100:
        tens = number // 10 * 10
        units = number % 10
        return f"{chislo[tens]}-{chislo[units]}"

    if number < 1000:
        hundreds = number // 100
        remainder = number % 100
        if remainder == 0:
            return f"{chislo[hundreds]} hundred"
        else:
            return f"{chislo[hundreds]} hundred and {number_in_english(remainder)}"

    return