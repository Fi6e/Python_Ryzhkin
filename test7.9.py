def is_lucky_ticket(ticket_number):
    # Конвертуємо номер квитку в рядок
    ticket_str = str(ticket_number)
    
    
    length = len(ticket_str)
    
    
    if length % 2 == 0:
        # якщо парна, все ок, ділимо на дві половини
        half_length = length // 2
        first_half = ticket_str[:half_length]
        second_half = ticket_str[half_length:]
    else:
        # якщо непарна кількість чисел, в цьому випадку ігнорується цифра посередині та ділиться порівну (число посередині ми записуємо до правої половини)
        half_length = length // 2
        first_half = ticket_str[:half_length]
        second_half = ticket_str[half_length + 1:]
    
    # Суми в двох половинах
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    
    # Перевірка суми
    return sum_first_half == sum_second_half


ticket_number = input("Введіть номер квитку: ")
is_lucky = is_lucky_ticket(ticket_number)
print(is_lucky)  
