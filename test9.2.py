def num_to_words(num):
    ones = ["", "одна", "дві", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять", "десять", "одинадцять",
            "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять",
            "дев'ятнадцять"]
    tens = ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"]
    hundreds = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот", "вісімсот", "дев'ятсот"]
    thousands = ["", "тисяча", "тисячі", "тисяч"]
    millions = ["", "мільйон", "мільйона", "мільйонів"]

    def convert_to_words(n, is_plural=False):
        if n == 0:
            return ""
        elif n < 20:
            if is_plural and n == 1:
                return ones[n] + "а"
            else:
                return ones[n]
        elif n < 100:
            tens_digit = n // 10
            ones_digit = n % 10
            if ones_digit == 0:
                return tens[tens_digit]
            else:
                return tens[tens_digit] + " " + ones[ones_digit]
        else:
            hundreds_digit = n // 100
            remainder = n % 100
            if remainder == 0:
                return hundreds[hundreds_digit]
            else:
                return hundreds[hundreds_digit] + " " + convert_to_words(remainder, True)

    integer_part = int(num)
    fractional_part = int((num - integer_part) * 100)
    result = ""

    if integer_part == 0:
        result = "нуль"
    else:
        millions_part = integer_part // 1000000
        thousands_part = (integer_part // 1000) % 1000
        ones_part = integer_part % 1000

        if millions_part > 0:
            result += convert_to_words(millions_part) + " " + millions[
                3 if 10 <= millions_part % 100 <= 20 else millions_part % 10] + " "
        if thousands_part > 0:
            result += convert_to_words(thousands_part) + " " + thousands[
                3 if 10 <= thousands_part % 100 <= 20 else thousands_part % 10] + " "
        if ones_part > 0:
            result += convert_to_words(ones_part) + " "

    result += "гривень"

    if fractional_part > 0:
        result += " " + convert_to_words(fractional_part) + " копійок"

    return result


# Приклад використання

# Введення грошової суми з клавіатури
num = float(input("Введіть грошову суму: "))
words = num_to_words(num)
print(f"Вхід: {num:.2f}. Вихід: {words}")

