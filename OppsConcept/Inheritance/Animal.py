# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Initialize parent class
        self.breed = breed      # Additional attribute for child class

    def meow(self):             # New method for child class
        print(f"{self.name} is meowing.")

# Create an object of the child class
my_cat = Cat("Whiskers", "Siamese")

# Access inherited and new attributes and methods
my_cat.eat()    # Output: Whiskers is eating.
my_cat.meow()   # Output: Whiskers is meowing.
print(my_cat.breed)  # Output: Siamese