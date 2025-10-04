# Madlibs Game

'''
adjective1 = input("adj1: ")
adjective2 = input("adj2: ")
adjective3 = input("adj3: ")
noun1 = input('noun1: ')
verb1 = input('verb1(-ing): ')

print(f'Today i went to a {adjective1} zoo')
print(f'In an exhibit, I saw a {noun1}')
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
'''

'''
num = 15

result = "Even" if num % 2 == 0 else "Odd"
print(result)
'''

'''
name = input()
while name == "":
    print('ss')
    name = input()
print(name)
'''

'''
principle = 0
rate = 0
time = 0
while True:
    principle = float(input('p = '))
    if principle <= 0:
        print('p != 0')
    else:
        break
    
while True:
    rate = float(input('r = '))
    if rate < 0:
        print('r != 0')
    else:
        break

while True:
    time = int(input('t = '))
    if time < 0:
        print('t != 0')
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(total)
'''

'''
for x in reversed(range(1,11)):
    print(x)
print('Hap')
'''

''' # timer
import time

my_time = int(input('Time:'))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/360)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print('Sleep')
'''

'''
def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')

display_invoice('BroCode', 42.50, "01/02")'''

'''
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(3,2,1,3,1,3,3,34))'''

'''def print_address(**kwargs):
    for key,value in kwargs.times():
        print(f"{key}:{value}")

print_address(street='123 Fake St.',
              state='Detroit',
              city='MI',
              zip='54321')'''

'''def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city'), {kwargs.get('zip')}}")

shipping_label("Muhamad", 'Sodiq', street='Oltinkol', city='Seoul', zip=1213)'''

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [pow(square, 2) for square in range(1, 11)]

"""
fruits = ['apple', 'banana', 'orange', 'coconut']
fruits = [fruit.upper() for friut in fruits]
"""

'''
def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
print(is_weekend('Sunday'))'''

'''import example

result = example.pi
result = example.cube(14)
print(result)'''


'''def favourite_food(food):
    print(f'Your favourite food is {food}')

def main():
    print('This is the main file')
    favourite_food("pizza")
    print('Good Bye!')

if __name__ == '__main__':
    main()
'''

# @property method

'''
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('Width must be greater than zero')
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print('Height must be greater than zero')

    @width.deleter
    def width(self):
        del self._width
        print("Width was deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height was deleted")

rectangle1 = Rectangle(3,4)

rectangle1.width = 5
rectangle1.height = 5
print(rectangle1.width)
print(rectangle1.height)

del rectangle1.width
del rectangle1.height
'''

# Decorator functions
'''
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print('** You add sprinkles **')
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print('** You add fudge **')
        func(*args, **kwargs)
    return wrapper
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f'Here is your {flavor} ice cream __')

get_ice_cream('vanilla')
'''

# exception: 1.try; 2.except; 3.finally
'''try:
    number = int(input('Enter a number'))
    print(1/number)
except ZeroDivisionError:
    print('You cant devide by zero ODOP!')
except ValueError:
    print('Enter only numbers')
except Exception:
    print('Something went wrong')
finally:
    print('DO some cleanup here!')'''

# Working with files
'''import os 

file_path = 'test.txt'

if os.path.exists(file_path):
    print(f"The location '{file_path} exist'")
    if os.path.isfile(file_path):
        print('That is a file')
    elif os.path.isdir(file_path):
        print('That is a directory')
else:
    print('The location doesnt exist')'''

# Writing files

'''txt_data = 'I like pizza!'
employees = ['Ali1', 'Ali2', 'Ali3', 'Ali4']
file_path = 'output.txt'

try:
    with open(file_path,'a') as file:
        for employee in employees:
            file.write(employee + ' ')
        print(f'txt file "{file_path}" was created')
except FileExistsError:
    print('That file already exists!')'''

'''import json

employee = {
    'name': 'Ali1',
    'age': 30,
    'job': 'cook'
}

file_path = 'output2.json'

try:
    with open(file_path, 'w') as file:
        json.dump(employee, file, indent=4)
        print('Json file was created')
except FileExistsError:
    print('that already exists')'''

import csv
employees = [['Name', 'Age', "Job"],
             ['Ali', 30, 'Cook'],
             ['Bobur', 40, 'Cashier'],
             ['Snady', 25, 'Scientist']]

file_path = 'output3.csv'

try:
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f'csv file "{file} was created"')
except FileExistsError:
    print('That file already exists! ')