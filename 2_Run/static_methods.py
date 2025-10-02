class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
        return position in valid_positions

employee1 = Employee('Eugene', 'Manager')
employee2 = Employee('Squidward', 'Cashier')
employee3 = Employee('Spongebob', 'Cook')


print(Employee.is_valid_position('Cook'))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

class Employee:
    company_name = "Tech Corp"   # class variable (shared by all employees)
    employee_count = 0           # tracks how many employees created

    def __init__(self, name, salary):
        self.name = name        # instance variable (unique per employee)
        self.salary = salary
        Employee.employee_count += 1

    # Instance method → works on one specific object
    def show_info(self):
        return f"{self.name} works at {Employee.company_name} earning ${self.salary}"

    # Class method → works on the class (affects all employees)
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    # Class method as "alternative constructor"
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

    # Static method → independent helper, doesn’t use self or cls
    @staticmethod
    def is_high_salary(salary):
        return salary > 5000


# ---------------- Using the class ----------------

e1 = Employee("Alice", 4000)
e2 = Employee("Bob", 7000)


e3 = Employee.from_string("Charlie-6000")

print(e1.show_info())
print(e2.show_info())
print(e3.show_info()) 

Employee.change_company("FutureTech")
print(e1.show_info())

print(Employee.is_high_salary(4000))
print(Employee.is_high_salary(7000))

print("Total employees:", Employee.employee_count)