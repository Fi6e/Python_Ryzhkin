def try1(highdoor, width_door, a, b, c):
    # Висота коробки менша або рівна висоті дверей
    if a <= highdoor:
        # Ширина коробки менша або рівна ширині дверей
        if b <= width_door:
            # Довжина коробки менша або рівна іншій стороні дверей
            if c <= highdoor or c <= width_door:
                return True
    # Якщо жодна з умов не виконується, коробку не можна помістити через двері
    return False

# Запит користувача для введення даних
highdoor = float(input("Введіть висоту дверей: "))
width_door = float(input("Введіть ширину дверей: "))
a = float(input("Введіть висоту коробки: "))
b = float(input("Введіть ширину коробки: "))
c = float(input("Введіть довжину коробки: "))

if try1(highdoor, width_door, a, b, c):
    print("Коробку можна пронести через двері.")
else:
    print("Коробку не можна пронести через двері.")
    




