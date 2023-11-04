def calculate_future_value(initial_amount, annual_interest_rate, years, monthly=False):
    #десятковий формат
    annual_interest_rate /= 100
    
    if monthly:
        # Якщо оновлення рахунку відбувається щомісяця, перетворюємо процентну ставку на щомісячну
        monthly_interest_rate = annual_interest_rate / 12
       
        months = years * 12
        # Формула складного відсотка для щомісячного поповнення
        future_value = initial_amount * ((1 + monthly_interest_rate) ** months)
    else:
        # Обчислення суми за формулою складного відсотку
        future_value = initial_amount * ((1 + annual_interest_rate) ** years)
    
    return future_value


initial_amount = float(input("Введіть початкову суму: "))
annual_interest_rate = float(input("Введіть річну процентну ставку (у відсотках): "))
years = float(input("Введіть тривалість депозиту в роках: "))
monthly = input("Чи оновлення рахунку відбувається щомісяця? (Так/Ні): ").strip().lower() == "так"
future_value = calculate_future_value(initial_amount, annual_interest_rate, years, monthly)

print(f"Сума на момент завершення депозиту: ${future_value:.2f}")
