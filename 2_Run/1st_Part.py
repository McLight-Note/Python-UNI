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

