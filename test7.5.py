def count_vowels(text):
    # Створюємо множину з голосними літерами
    vowels = set("aeiouyAEIOUY")
    vowel_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1

    return vowel_count

text = input("Введыть речення: ")
vowel_count = count_vowels(text)
print("Кількість голосних літер в тексті:", vowel_count)
