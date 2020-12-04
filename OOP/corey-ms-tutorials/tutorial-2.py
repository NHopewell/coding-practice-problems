# class variables 

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay

        Employee.num_of_employees += 1

    def display_fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


employee_1 = Employee('Nick', 'Hopewell', 50000)

Employee.raise_amount = 1.05
print(employee_1.__dict__)

employee_1.raise_amount = 1.05
print(employee_1.__dict__)

print(Employee.num_of_employees)