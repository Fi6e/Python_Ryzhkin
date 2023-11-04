def int_to_roman(number):
    if not 0 <= number < 4000:
        raise ValueError("Число має бути в діапазоні від 0 до 3999")

    # арабські >>> римські
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    result = ""
   
    arabic_numbers = sorted(roman_numerals.keys(), reverse=True)

    while number > 0:
        for arabic in arabic_numbers:
            if number >= arabic:
                result += roman_numerals[arabic]
                number -= arabic
                break

    return result

def roman_to_int(roman):
    # римські >>> арабські
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_numerals[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result


number = 1987
roman = int_to_roman(number)
print(f'{number} у римському форматі: {roman}')

roman_numeral = 'MCMLXXXV'
integer = roman_to_int(roman_numeral)
print(f'{roman_numeral} у арабському форматі: {integer}')
