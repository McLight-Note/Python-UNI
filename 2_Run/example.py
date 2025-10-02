pi = 3.14159

def square(x):
    return x**2

def cube(x):
    return x**3

def circum(radius):
    return 2*pi*radius

def area(radius):
    return pi * radius ** 2

from st_Part import *

def fav_drink(drink):
    print(f'Your favourite drink is {drink}')

def main():
    print('This is example.py')
    favourite_food('pizza"s')
    fav_drink('coffee')
    print('GB')

if __name__ == "__main__":
    main()