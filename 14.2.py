import pickle
import os

# Ім'я файлу для зберігання даних
PHONEBOOK_FILE = 'phonebook.pkl'

# Функція для створення нового запису
def add_contact(phonebook):
    name = input("Введіть ім'я абонента: ")
    last_name = input("Введіть прізвище абонента: ")
    phone_number = input("Введіть номер телефону: ")
    contact = {"name": name, "Прізвище": last_name, "Номер": phone_number}
    phonebook.append(contact)
    print("Контакт успішно доданий.")

# Функція для видалення запису за іменем
def delete_contact_by_name(phonebook):
    name = input("Введіть ім'я абонента для видалення: ")
    contacts_to_delete = [contact for contact in phonebook if contact["name"] == name]
    if contacts_to_delete:
        for contact in contacts_to_delete:
            phonebook.remove(contact)
        print(f"Видалено {len(contacts_to_delete)} контактів з іменем '{name}'.")
    else:
        print(f"Контакт з ім'ям '{name}' не знайдений.")

# Функція для видалення запису за номером телефону
def delete_contact_by_number(phonebook):
    number = input("Введіть номер телефону для видалення: ")
    contacts_to_delete = [contact for contact in phonebook if contact["Номер"] == number]
    if contacts_to_delete:
        for contact in contacts_to_delete:
            phonebook.remove(contact)
        print(f"Видалено {len(contacts_to_delete)} контактів з номером '{number}'.")
    else:
        print(f"Контакт з номером '{number}' не знайдений.")

# Функція для виведення всіх контактів
def view_all_contacts(phonebook):
    if not phonebook:
        print("Телефонна книга порожня.")
    else:
        for i, contact in enumerate(phonebook, start=1):
            print(f"{i}. Ім'я: {contact['name']}, Прізвище: {contact['Прізвище']}, Номер: {contact['Номер']}")

# Головна функція програми
def main():
    # Перевіряємо, чи існує файл телефонної книги
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, 'rb') as file:
            phonebook = pickle.load(file)
    else:
        phonebook = []

    while True:
        print("\nОберіть опцію:")
        print("1. Додати контакт")
        print("2. Видалити контакт за іменем")
        print("3. Видалити контакт за номером телефону")
        print("4. Пошук за іменем")
        print("5. Пошук за номером телефону")
        print("6. Переглянути всі контакти")
        print("7. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            delete_contact_by_name(phonebook)
        elif choice == '3':
            delete_contact_by_number(phonebook)
        elif choice == '4':
            name = input("Введіть ім'я для пошуку: ")
            matching_contacts = [contact for contact in phonebook if contact["name"] == name]
            if matching_contacts:
                for contact in matching_contacts:
                    print(f"Ім'я: {contact['name']}, Прізвище: {contact['Прізвище']}, Номер: {contact['Номер']}")
            else:
                print(f"Контакти з іменем '{name}' не знайдені.")
        elif choice == '5':
            number = input("Введіть номер телефону для пошуку: ")
            matching_contacts = [contact for contact in phonebook if contact["Номер"] == number]
            if matching_contacts:
                for contact in matching_contacts:
                    print(f"Ім'я: {contact['name']}, Прізвище: {contact['Прізвище']}, Номер: {contact['Номер']}")
            else:
                print(f"Контакти з номером '{number}' не знайдені.")
        elif choice == '6':
            view_all_contacts(phonebook)
        elif choice == '7':
            with open(PHONEBOOK_FILE, 'wb') as file:
                pickle.dump(phonebook, file)
            print("Дякуємо за використання програми. Дані збережено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
