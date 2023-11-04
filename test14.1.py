class Record:
    def __init__(self, title, deadline, comment, priority, tags=[]):
        self.title = title
        self.deadline = deadline
        self.comment = comment
        self.priority = priority
        self.tags = tags
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        status = "Виконано." if self.is_done else "Не виконано!"
        return f"Заголовок: {self.title}\nДедлайн: {self.deadline}\nКоментарій: {self.comment}\nПріоритет: {self.priority}\nСтатус: {status}\nТег: {', '.join(self.tags)}"


class Planner:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, title):
        for record in self.records:
            if record.title == title:
                self.records.remove(record)

    def modify_record(self, title, new_title, new_deadline, new_comment, new_priority):
        for record in self.records:
            if record.title == title:
                record.title = new_title
                record.deadline = new_deadline
                record.comment = new_comment
                record.priority = new_priority

    def display_records(self):
        for record in self.records:
            print(record)
            print("=" * 30)

    def search_by_tag(self, tag):
        matching_records = [record for record in self.records if tag in record.tags]
        if matching_records:
            for record in matching_records:
                print(record)
                print("=" * 30)
        else:
            print("Записів з цим тегом не знайдено.")


if __name__ == "__main__":
    planner = Planner()

    while True:
        print("Меню списку справ:")
        print("1. Додати справу")
        print("2. Видалити справу")
        print("3. Змінити запис")
        print("4.Позначити справу як виконану")
        print("5. Перегляд справ")
        print("6. Пошук за тегом")
        print("7. Вихід")

        choice = input("Введіть команду: ")

        if choice == '1':
            title = input("Введіть назву (заголовок): ")
            deadline = input("Введіть Дедлайн: ")
            comment = input("Додайте коментар: ")
            priority = input("Визначіть пріоритет: ")
            tags = input("Введіть теги(через кому): ").split(',')
            record = Record(title, deadline, comment, priority, tags)
            planner.add_record(record)
            print("Запис успішно був додатий.")

        elif choice == '2':
            title = input("Введіть назву (заголовок) для видалення: ")
            planner.remove_record(title)
            print("Запис успішно видалено.")

        elif choice == '3':
            title = input("Введіть назву (заголовок) для змінення: ")
            new_title = input("Введіть нову назву: ")
            new_deadline = input("Введіть новий дедлайн: ")
            new_comment = input("Додайте новий коментар: ")
            new_priority = input("Визначте новий пріоритет: ")
            planner.modify_record(title, new_title, new_deadline, new_comment, new_priority)
            print("Запис успішно змінено.")

        elif choice == '4':
            title = input("Введіть назву запису щоб відмітити як виконаний: ")
            for record in planner.records:
                if record.title == title:
                    record.mark_as_done()
                    print("Запис успішно виконаний.")
                    break

        elif choice == '5':
            planner.display_records()

        elif choice == '6':
            tag = input("Введіть тег для пошуку: ")
            planner.search_by_tag(tag)

        elif choice == '7':
            break

        else:
            print("Неправильний ввід, введіть коректну назву.")
