import math


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))


discriminant = b**2 - 4*a*c


if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real values: {x1} and {x2}")
elif discriminant == 0:
    x = -b / (2*a)
    print(f"One real x: {x}")
else:
    part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    x1 = complex(part, imaginary_part)
    x2 = complex(part, -imaginary_part)
    print(f"Two complex values: {x1} and {x2}")
