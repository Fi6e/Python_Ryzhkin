def random_number_generator(seed):
    while True:
        
        seed_str = str(seed)
        y_str = seed_str[3:] + seed_str[:3]
        y = int(y_str)

        # Перемножуємо seed та Y
        product = seed * y
        result = (product // 1000) % 1000000

        # Встановлюємо отримане значення як новий seed для наступного ітерації
        seed = result

        yield result  

initial_seed = 654321  

generator = random_number_generator(initial_seed)

for _ in range(10):
    random_number = next(generator)
    print(random_number)
