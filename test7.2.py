def is_palindrome(phrase):
    # нижній регістр і видаляємо пробіли та розділові знаки
    phrase = ''.join(filter(str.isalnum, phrase.lower()))
    
    # Порівнюємо фразу з її оберненим варіантом
    return phrase == phrase[::-1]


input_phrase = input("Введіть речення:")
result = is_palindrome(input_phrase)
print(result)  
