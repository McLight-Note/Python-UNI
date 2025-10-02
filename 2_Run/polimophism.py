from abc import ABC, abstractmethod

# convert a normal class to a abstract class

# Duck typing = concept where the class of an object is less important than the methods / attributes
#               class type is not checked if minimum methods / attributes are present
#               "if it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")

class Chicken:

    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is clucking")

class Person:

    def catch(self, duck:Duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

# because the Chicken class has the similar attributes / methods as the Duck class
# so you can also pass chicken instance to the function

person.catch(chicken)

'''
class Shape():
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, raduis):
        self.radius = raduis
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, raduis):
        super().__init__(raduis)
        self.topping = topping

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza('pepperoni', 15)]

for shape in shapes:
    print(f'{shape.area()}cm.sqr')
'''