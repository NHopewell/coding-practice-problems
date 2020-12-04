# dunder methods

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
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() in (5,6):
            return False
        return True

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.display_fullname()}: {self.email}" 

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.display_fullname())


employee_1 = Employee("nick", "hopewell", 50000)
employee_2 = Employee("John", "smith", 60000)

# __repr__ and __str__
print(repr(employee_1))
print(employee_1)

# __add__
print(employee_1 + employee_2)

# __len__
print(len(employee_1))