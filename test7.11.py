def sort_words_by_length(text):
    # Розділити рядок на слова
    words = text.split()
    
    # Відсортувати слова за довжиною, використовуючи len() як ключ
    sorted_words = sorted(words, key=len)
    
    # Повернути список 
    return ' '.join(sorted_words)


text = input("Введіть рядок: ")
sorted_text = sort_words_by_length(text)
print(sorted_text)
