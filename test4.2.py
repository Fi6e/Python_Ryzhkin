import math as m
x = float(input('Введіть значення х: '))
u = float(input('Введіть значення u: '))
q = float(input('Введіть значення q: '))
# pi = 3.14
pi = m.pi
Step1 =1/(q * m.sqrt(2*pi))
Step2 = m.exp(-1* (m.pow((x - u),2)/2 * m.pow(q,2)))
result = Step1 * Step2
print(f'Result: {result}')