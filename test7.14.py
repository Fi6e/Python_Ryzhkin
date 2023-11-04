import re

def is_valid_email(email):
    # Регулярний вираз для перевірки коректності e-mail адреси (взято з інтернету)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # https://fotocvetov.com/allinnews/irc&com&uu/info/2020/02/uk/vyrazenie-perevirka-python-na-dijsnu-adresu-elektronnoi-posti/ 
    
    # Перевірка за допомогою регулярного виразу
    if re.match(pattern, email):
        return True
    else:
        return False


email = input("Введіть e-mail адресу: ")
if is_valid_email(email):
    print("E-mail адреса коректна.")
else:
    print("E-mail адреса некоректна.")
