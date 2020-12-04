class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@company.com"
        self.pay = pay

    def display_fullname(self):
        return f"{self.first} {self.last}"


employee_1 = Employee('Nick', 'Hopewell', 50000)

print(employee_1.first)
print(employee_1.display_fullname())
