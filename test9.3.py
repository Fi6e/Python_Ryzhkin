def text_to_morse(text):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        ' ': ' '
    }

    morse_text = ""
    text = text.upper()

    for char in text:
        if char in morse_code:
            morse_text += morse_code[char] + " "
        else:
            morse_text += "/ "

    return morse_text

# Приклад використання
input_text = input("Введіть текст: ")
morse_result = text_to_morse(input_text)
print("Морзе-код для введеного тексту:")
print(morse_result)
