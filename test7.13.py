def can_construct_string(s1, s2):
    # Лічильник
    count_s1 = {}
    count_s2 = {}
    
    # Перетворити обидва рядки до нижнього регістру
    s1 = s1.lower()
    s2 = s2.lower()
    
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1
    
    for char in s2:
        count_s2[char] = count_s2.get(char, 0) + 1
    
    # Перевірка
    for char in count_s2:
        if char not in count_s1 or count_s2[char] > count_s1[char]:
            return False
    
    return True

s1 = input("Введіть перший рядок: ")
s2 = input("Введіть другий рядок: ")
result = can_construct_string(s1, s2)
print(result)
