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


# use set_raise_amount class method
Employee.set_raise_amount(1.07)
employee_1 = Employee('Nick', 'Hopewell', 50000)

print(employee_1.pay)
employee_1.apply_raise()
print(employee_1.pay)

# use from_string as an alternative constructor
employee_2 = Employee.from_string('nick-hopewell-50000')
print(employee_2.first)

# use static method
import datetime
my_date = datetime.date(2020, 11, 13)
print(Employee.is_workday(my_date))