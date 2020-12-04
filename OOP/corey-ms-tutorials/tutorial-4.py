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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)

        self.programming_language = programming_language


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if not employees:
            self.employees = []
        else:
            assert(all(isinstance(employee, Employee) for employee in employees)
                ), TypeError("May only pass objects of type Employee to employees")
            self.employees = employees

    def add_employee(self, employee):
        assert(isinstance(employee, Employee)
        ), TypeError("Can only pass Employees to add_employee()")

        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.display_fullname())


## Developer
#print(help(Developer))
dev_1 = Developer('Nick', 'Hopewell', 50000, 'Python')
dev_2 = Developer('Mary', 'Smith', 60000, 'JavaScript')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.programming_language)

## Manager
steven = Manager('Steven', 'Wu', 1000000, employees = [dev_1, dev_2])
print(steven.employees[0].first)

steven.print_employees()

dev_3 = Developer('John', 'Smith', 20000, 'Java')
steven.add_employee(dev_3)
steven.print_employees()