# для порожнього списку
def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
# медіана та середнє значення
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        # Якщо кількість елементів парна
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        # Якщо кількість елементів непарна
        median = sorted_numbers[n // 2]
    
    return median

# Ввід чисел з клавіатури
numbers = []
while True:
    try:
        num = float(input("Введіть число (або Enter, щоб завершити введення): "))
        numbers.append(num)
    except ValueError:
        break

if len(numbers) == 0:
    print("Список порожній. Неможливо обчислити середнє значення і медіану.")
else:
    avg = calculate_average(numbers)
    median = calculate_median(numbers)
    print(f"Середнє значення: {avg}")
    print(f"Медіана: {median}")
