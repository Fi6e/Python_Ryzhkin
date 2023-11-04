import math as m
a = float(input('Введіть значення а: '))
b = float(input('b Введіть значення b: '))
# експонента
e = m.e
Step1 = m.sqrt(a*b)
Step2 = m.pow(e,a)*b
Step3 = a*m.pow(e,(2*a)/b)
result = (Step1/Step2) + Step3
print(f'Result: {result}')