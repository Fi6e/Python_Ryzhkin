import random


class Employee:
    def __init__(self, id, first_name, second_name, rate):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.rate = rate

    def get_salary(self):
        pass

    def get_taxes(self):
        pass

    def __repr__(self):
        return "{" + str(self.id) + ", " + \
            self.second_name + ", " + \
            str(self.salary) + ", " + \
            str(self.taxes) + "}"


class HourEpm(Employee):
    def __init__(self, id, first_name, second_name, rate):
        super().__init__(id, first_name, second_name, rate)
        self.salary = self.get_salary()
        self.taxes = self.get_taxes()

    def get_salary(self):
        return self.rate

    def get_taxes(self):
        return self.get_salary() * (0.18 + 0.015)


class FixPayEmp(Employee):
    def __init__(self, id, first_name, second_name, rate):
        super().__init__(id, first_name, second_name, rate)
        self.salary = self.get_salary()
        self.taxes = self.get_taxes()

    def get_salary(self):
        return self.rate

    def get_taxes(self):
        return self.get_salary() * (0.18 + 0.015)


class FOP(Employee):
    def __init__(self, id, first_name, second_name, rate):
        super().__init__(id, first_name, second_name, rate)
        self.salary = self.get_salary()
        self.taxes = self.get_taxes()

    def get_salary(self):
        result = 20.8 * 8 * self.rate
        return result + result * 0.1

    def get_taxes(self):
        return self.get_salary() * 0.05 + 704


class SelfEmp(Employee):
    def __init__(self, id, first_name, second_name, rate, lines):
        super().__init__(id, first_name, second_name, rate)
        self.salary = self.get_salary(lines)
        self.taxes = self.get_taxes()

    def get_salary(self, lines):
        return lines * self.rate

    def get_taxes(self):
        return self.salary * (0.18 + 0.015) + 704


def generator(n):
    names = ["Max", "Oleksandr", "Katia", "Vitia", "Ksenia", "Mohammad", "Nikita", "Juro"]
    second_names = ["Voloshchuk", "Ryzhkin", "Matenko", "Kus", "Ryzun", "Posternak", "Vovchenko" , "Romaniv"]

    employees = []

    for i in range(1, n):
        name = random.choice(names)
        second_name = random.choice(second_names)
        id = i
        if not i % 4:
            emp = HourEpm(id, name, second_name, random.randint(50, 400))
        elif not i % 3:
            emp = FixPayEmp(id, name, second_name, random.randint(6000, 50_000))
        elif not i % 2:
            emp = FOP(id, name, second_name, random.randint(50, 400))
        else:
            emp = SelfEmp(id, name, second_name, random.randint(1, 50), random.randint(500, 20_000))

        employees.append(emp)

    return employees


def sort(emp_list):
    size = len(emp_list)
    for i in range(size):
        min_inx = i
        for j in range(i + 1, size):
            if emp_list[j].salary < emp_list[min_inx].salary:
                min_inx = j
            elif emp_list[j].salary == emp_list[min_inx].salary and emp_list[j].second_name < emp_list[
                min_inx].second_name:
                min_inx = j

        emp_list[i], emp_list[min_inx] = emp_list[min_inx], emp_list[i]


if __name__ == "__main__":
    n = int(input("Input the count of employees\n>> "))
    lst = generator(n)
    print("Sorted list:", lst, sep="\n")

