#Using functions
#These are functions without parameters.
#Uses def as the keyword(def means define)
#create a function that returns your course_unit and name
def my_course_unit():
    print("programming_in_python")

def my_name():
    print("fortunate_gloria")
#calling the function so that it performs the task
my_course_unit()
my_name()

#Parameters/Arguements
#create a function that multiplies two numbers a and b where a=3 and b=10

def product_of_two_numbers(a , b):
    output = a * b
    print(f"The product of {a}and {b} is {output}")
product_of_two_numbers(3, 10)
product_of_two_numbers(4, 20)
product_of_two_numbers(5, 100)

#create a function that returns your name and your age
def my_name_and_age(name, age):
    print(f"my name is {name} and i am {age} years old.")
my_name_and_age("fortunate", 27)


    


