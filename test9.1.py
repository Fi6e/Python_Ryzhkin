def blackjack(cards):
    card_values = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        'T': 10, 'J': 10, 'Q': 10, 'K': 10
    }

    total = 0
    aces = 0

    for card in cards:
        if card == 'A':
            aces += 1
        else:
            total += card_values.get(card, 0)

    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    if total <= 21:
        return total
    else:
        return 'Bust'


input_cards = input("Введіть карти гравця (без пробілів): ").upper()

cards = list(input_cards)

result = blackjack(cards)
print(f"Результат: {result}")