def simple_encrypt(message):
    
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Перевіряємо, чи символ є літерою
            if char == 'z':
                encrypted_char = 'a'  # Якщо 'z', то 'a'
            elif char == 'Z':
                encrypted_char = 'A'  # Якщо 'Z', 'A'
            else:
                # Замінюємо літеру на наступну в алфавітному порядку
                encrypted_char = chr(ord(char) + 1)
        else:
            # Якщо символ не є літерою, залишаємо його
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message


message = input("Введіть повідомлення:")
encrypted_message = simple_encrypt(message)
print(encrypted_message)
