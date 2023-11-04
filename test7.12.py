import re

def remove_extra_spaces(text):
    # Використовуємо регулярний вираз для видалення зайвих пробілів
    cleaned_text = re.sub(r'\s+', ' ', text).strip()    #Функція взята з інтернету
    
    return cleaned_text

# Приклад використання функції:
text = input("Введіть рядок: ")
cleaned_text = remove_extra_spaces(text)
print(cleaned_text)
