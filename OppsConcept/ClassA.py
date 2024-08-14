# Define a class
class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def bark(self):       # Method
        print(f"{self.name} is barking.")

# Create an object
my_dog = Dog("Buddy", 5)

# Access attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 5
my_dog.bark()       # Output: Buddy is barking.
