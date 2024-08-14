# person.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def is_adult(self):
        return self.age >= 18

# Example usage
if __name__ == "__main__":
    person = Person("Alice", 30)
    person.introduce()  # Output: Hello, my name is Alice and I am 30 years old.
    print(person.is_adult())  # Output: True
