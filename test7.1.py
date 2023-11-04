def rotate_string(input_string, k):
    # Перевірка на випадок, якщо k дорівнює 0
    if k == 0:
        return input_string

    # Знаходимо довжину рядка
    length = len(input_string)

    # Нормалізуємо k, 
    k = k % length

    # Використовуємо зрізи, щоб виконати обертання рядка
    rotated_string = input_string[k:] + input_string[:k]

    return rotated_string

input_string = input("Введіть рядок: ")
k = int(input("Введіть значення k: "))

result = rotate_string(input_string, k)
print(result)

