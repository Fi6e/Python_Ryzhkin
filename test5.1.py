def check(n):
    # Число повинно бути додатнім
    if n <= 0:
        return False
    
    # Бітова операція
    return (n & (n - 1)) == 0
10
a = int(input("Введіть ціле додатнє число: "))

if check(a):
    print(f"{a} є степенем двійки.")
else:
    print(f"{a} не є степенем двійки.")
