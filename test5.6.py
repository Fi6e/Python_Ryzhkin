def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if is_triangle(a, b, c):
    print("Такий трикутник існує.")
else:
    print("Такий трикутник не існує.")
