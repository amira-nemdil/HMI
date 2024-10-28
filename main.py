#import greetings as gtg

#print(gtg.say_hello('Amira'))
#print(gtg.say_goodbye('Amira'))

from shapes
import circle_area, rectangle_area

print(circle_area(5))
print(rectangle_area(4, 2))

# Defining a basic class
class Animal:
    # Constructor to initialize the name
def __init__(self, name):
    self.name = name

# Method to describe the animal
def describe(self):
    return f "I am an animal named {self.name} "


# Creating an object of the Animal Class
animal = Animal("Lion")
print(animal.describe()) #Output: I am an animal named Lion
print(animal.name)

# Derived Class(Child) - inherits From Animal
class Cat(Animal):
    # Method
for the dog to speak
def speak(self):
    return f "{self.name} says meow!"



# Overriding the describe method
def describe(self):
    return f "I am a fluffy brownie cat named {self.name}"

# Creating an object of the Cat class
cat = Cat("Adel")
print(cat.describe()) # Output: I am a fluffy brownie cat named Adel
print(cat.speak()) # Output: Adel says meow!




    from shapes
import Child, Parent

# parent_object = Parent()
child_object = Child()
print(child_object.value) # Output: Child value


class Parent:
    def show(self):
    print("this is the Parent class ")

class Child(Parent):
    def show(self):
    #call the method from Parent Class
super().show()
print("This si the child class")

child_object = Child()
child_object.show()
#Output:
    # This is the Parent class
# This is the Child class

class Parent:
    def __init__(self):
    self.value = " Parent value "

class Child(Parent):
    def __init__(self):
    super().__init__() #call the parent constructor
self.value = "Child value"

child_object = Child()
print(child_object.value) #output: Child value







#DECORATORS

class MyClass:
    @staticmethod
def static_method():
    print(" This is a static  method ")

MyClass.static_method() #Called without an instance(without using object and self())



class Myclass:
    @classmethod
def class_method(cls):
    print(f " This is a class method.class : {cls} ")

Myclass.class_method() # Can be used called without an instance







class MeinClass:
    def __init__(self, value):
    self.value = value #value here is an attribute

@property #transform it into an attribute % 50
def value2(self): #value2 here is a method
return self.value #and here it became an attribute

@value2.setter #Transfomred into attribute % 100
def value2(self, new_value):
    self.value = new_value


# Usage
obj = MeinClass(10)
print(obj.value) #Access value like an attribute
obj.value2 = 20 # Uses the setter to update value
print(obj.value2) # Access value lke an attribute





# Polymorphism:
# declaring a class without finishing it to just run the code corrctly and edit it later: use ... three dots or pass
# example : 
class Animal : 
  ''' this is a module of '''
 pass
