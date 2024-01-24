import csv

class Employee:
    def __init__(self, id, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

    def __repr__(self):
        return f"Employee(id='{self.id}',name='{self.name}', age={self.age}, salary={self.salary})"


def sort_employees(employees, sorting_parameter):
    if sorting_parameter == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sorting_parameter == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sorting_parameter == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")


def print_employees(employees):
    for emp in employees:
        print(emp)


def main():
    sorting_parameter = int(
        input("Enter the sorting parameter (1. Age, 2. Name, 3. Salary): ")
    )
    with open("table_data.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Skip the headers
        employees = []
        for row in csv_reader:
            id, name, age, salary = row
            employees.append(Employee(id, name, int(age), float(salary)))
        sorted_employees = sort_employees(employees, sorting_parameter)
        print_employees(sorted_employees)


if __name__ == "__main__":
    main()
