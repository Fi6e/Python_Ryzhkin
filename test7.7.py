import re

def snake_to_camel(text):
    # Використовуємо регулярний вираз для пошуку слів у snake_case
    words = re.findall(r'\w+', text)
    
    # Перетворюємо слова в camelCase
    camel_case_words = [word.capitalize() if i > 0 else word for i, word in enumerate(words)]
    
    # Повертаємо результат, об'єднуючи слова разом
    return ''.join(camel_case_words)

# Приклад використання:
snake_case_str = "print([res_square ** 2 for res_square in input_array if res_square > 18 ])"
camel_case_result = snake_to_camel(snake_case_str)
print(camel_case_result)  # Виведе "MyVariableName"


def camel_to_snake(text):
    # Використовуємо регулярний вираз для знаходження верблюжихCase слів
    words = re.findall(r'[A-Za-z][a-z]*', text)
    
    # Перетворюємо слова в snake_case
    snake_case_words = '_'.join(words).lower()
    
    # Повертаємо результат
    return snake_case_words

# Приклад використання:
camel_case_str = "print([resSquare ** 2 for resSquare in inputArray if resSquare > 18 ])"
snake_case_result = camel_to_snake(camel_case_str)
print(snake_case_result)  # Виведе "my_variable_name"
