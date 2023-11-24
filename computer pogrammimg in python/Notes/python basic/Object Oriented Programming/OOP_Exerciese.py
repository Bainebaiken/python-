# create  a User class with properties ie name,age,location
class User:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

# Creating instances of the User class
user1 = User("baine", 30, "New York")
user2 = User("baiken", 25, "Los Angeles")

# Accessing and displaying user information
user1.display_info()
print()
user2.display_info()