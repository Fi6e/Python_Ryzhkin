from PIL import Image

def hide_text_in_bmp(input_image_path, output_image_path, text_to_hide):
    # Відкриваємо зображення
    image = Image.open(input_image_path)

    # Перетворюємо текст у бінарний формат
    text_binary = ''.join(format(ord(char), '08b') for char in text_to_hide)

    # Перевірка, чи можна приховати текст у зображенні
    if len(text_binary) > image.width * image.height * 3:
        raise ValueError("Розмір тексту перевищує об'єм зображення")

    data_index = 0

    # Проходимо по пікселях зображення та приховуємо бітовий текст
    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))

            for color_channel in range(3):  # (R, G, B)
                if data_index < len(text_binary):
                    pixel[color_channel] = int(bin(pixel[color_channel])[:-1] + text_binary[data_index], 2)
                    data_index += 1

            image.putpixel((x, y), tuple(pixel))

    # Зберігаємо зображення з прихованим текстом
    image.save(output_image_path)

# Приклад використання
input_image = "input_image.bmp"
output_image = "output_image.bmp"
text_to_hide = "Це текст, який буде приховано у зображенні."

hide_text_in_bmp(input_image, output_image, text_to_hide)
