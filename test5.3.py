import random

def checkwiner(player, bot):
    if player == bot:
        return "Нічия!"
    elif (player == "камінь" and bot == "ножиці") or \
         (player == "ножиці" and bot == "папір") or \
         (player == "папір" and bot == "камінь"):
        return "You win!"
    else:
        return "You Lose :("

while True:
    option = ["камінь", "ножиці", "папір"]
    bot = random.choice(option)
    
    player = input("Виберіть: камінь, ножиці, або папір (для виходу натисніть 'в'): ").lower()
    
    if player == 'в':
        break
    
    if player not in option:
        print("Ви ввели некоректну опцію. Спробуйте ще раз.")
        continue
    
    winer = checkwiner(player, bot)
    
    print(f"Ваш вибір: {player}")
    print(f"Комп'ютер вибрав: {bot}")
    print(winer)
