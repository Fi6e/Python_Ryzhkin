import random
import string

def generate_password():
    # min 1 number
    digits = ''.join(random.choice(string.digits) for _ in range(1))

    # min 1 special symbol
    special_chars = ''.join(random.choice(string.punctuation) for _ in range(1))

    # min 6 up and lower letters
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(6))

    # combinate and mix
    password = digits + special_chars + letters
    password = ''.join(random.sample(password, len(password)))

    # plus to password symbols or letters up to 8 
    while len(password) < 8:
        password += random.choice(string.ascii_letters)

    return password

# Generate and print
password = generate_password()
print("Згенерований пароль:", password)
