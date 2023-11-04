import math

def calculate_triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
     
        s = (a + b + c) / 2
        # Формула Герона 
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return "Трикутник з такими сторонами не існує."
    

# Запит користувача для введення довжин сторін
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

result = calculate_triangle_area(a, b, c)
print("S = ", result)
