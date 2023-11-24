#object-oriented programming is about creating objects that contain both data and methods.
# ADVANTAGES OF OOP
#OOP is faster and easier to execute
#OOP provides a clear structure for the programs
#OOP helps to keep the Kotlin code DRY "Don't Repeat Yourself", and makes the code easier to maintain, modify and debug
#OOP makes it possible to create full reusable applications with less code and shorter development time

 #CLASSES
#Classes and objects are the two main aspects of object-oriented programming.
#A Class is like an object constructor, or a "blueprint" for creating objects.

# HOW TO CREATE  class
#use the keyword class:
class MyClass:
  x = 5

print(MyClass)
#use the __init__() function to assign values for name and age
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("baine", 237)

print(p1.name)
print(p1.age)

class Person:# with out strg function
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("baine", 26)

print(p1)

class Person:# with a stg function
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("garvin", 36)

print(p1)