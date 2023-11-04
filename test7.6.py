def print_in_frame(text):
    width = len(text) + 4  # 2 left/right space
    border = '*' * width  # top / bottom

    print(border)  

    # text + 2 left/right space
    for line in text.splitlines():
        print(f'* {line} *')

    print(border)  

text = input("Введіть речення: ")
print_in_frame(text)
