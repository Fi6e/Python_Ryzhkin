from decimal import *
getcontext().prec = 6
income= Decimal(input('Введіть заробітню плату:'))
tax1 = income*Decimal(0.18)
tax2 = income*Decimal(0.015)
print(f'Total:\nВсього податку: {tax1+tax2}\nПодаток на фізичних осіб(18%): {tax1}\nВійськовий збір1 1.5%: {tax2}')