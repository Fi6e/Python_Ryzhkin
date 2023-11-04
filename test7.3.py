def is_valid_parentheses(s):
    stack = []
    # Словник, який містить відповідні пари дужок
    parentheses_dict = {')': '(', ']': '[', '}': '{', '>': '<'}

    for char in s:
        if char in parentheses_dict.values():  # Якщо це відкриваюча дужка
            stack.append(char)
        elif char in parentheses_dict.keys():  # Якщо це закриваюча дужка
            if not stack or stack.pop() != parentheses_dict[char]:
                return False  # Некорект

    return not stack  # Якщо стек пустий True


# Приклад використання функції:
sequence = input("Введіть рядок: ")
result = is_valid_parentheses(sequence)
print(result)  


