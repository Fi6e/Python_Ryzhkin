def calculate_years(initial_amount, target_amount, annual_interest_rate):
    years = 0
    while initial_amount < target_amount:
        initial_amount *= (1 + annual_interest_rate / 100)
        years += 1
    return years


initial_amount = float(input("Введіть початкову суму: "))
target_amount = float(input("Введіть потрібну суму: "))
annual_interest_rate = float(input("Введіть річний банківський процент (у відсотках): "))


years_needed = calculate_years(initial_amount, target_amount, annual_interest_rate)

print(f"Кількість років для досягнення потрібної суми: {years_needed} років")
