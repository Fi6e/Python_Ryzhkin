def find_last_person(N, K):
    people = list(range(1, N + 1))  # Створюємо список від 1 до N

    index = 0  # Початок
    while len(people) > 1:
        index = (index + K - 1) % len(people)  
        del people[index]  

    return people[0]  # Повертаємо номер залишившогося 


N = 10  
K = 3   
last_person = find_last_person(N, K)
print("Номер останньої залишеної людини:", last_person)
