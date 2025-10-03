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


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title & self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title | keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
    
    

book1 = Book('The Hobbit', 'J.R.R. Tolkien', 310)
book2 = Book('Haayr poter', 'Someone2', 223)
book3 = Book('Book2', 'Someone3', 172)
