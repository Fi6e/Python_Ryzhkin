
# Сортування вставками (insertion) 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


input_str = input("Введіть елементи масиву, розділених пробілами: ")
arr = [int(x) for x in input_str.split()]

insertion_sort(arr)
print("Відсортований масив:", arr)