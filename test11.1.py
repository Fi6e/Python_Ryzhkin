def calculate_bytes(log_file):
    sent_bytes = 0
    received_bytes = 0

    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 10:
                try:
                    sent_bytes += int(parts[9])
                    received_bytes += int(parts[10])
                except (ValueError, IndexError):
                    # Ігноруємо рядок, якщо не вдалося перетворити в ціле число
                    pass

    return sent_bytes, received_bytes

log_file = r'C:\Users\koshk\Downloads\log.txt'
sent_bytes, received_bytes = calculate_bytes(log_file)

print(f"Сумарно отримано байтів: {sent_bytes} байтів")
print(f"Сумарно надіслано байтів: {received_bytes} байтів")
