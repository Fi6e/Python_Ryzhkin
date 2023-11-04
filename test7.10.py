def shortest_word_length(text):
    # Розділити рядок на слова
    words = text.split()
    
    #змінна для зберігання довжини найкоротшого слова
    shortest_length = float('inf')  # початкове значення - нескінченність
    
    # Пройтися по кожному слову і знайти найкоротше
    for word in words:
        word_length = len(word)
        if word_length < shortest_length:
            shortest_length = word_length
    
    return shortest_length

text = input("Введіть рядок: ")
shortest_length = shortest_word_length(text)
print("Довжина найкоротшого слова в рядку:", shortest_length)
