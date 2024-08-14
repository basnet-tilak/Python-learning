# student.py

from Person import Person  # Import the Person class from person.py

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Initialize the parent class
        self.student_id = student_id  # New attribute for Student class

    def introduce(self):
        super().introduce()  # Call the parent class method
        print(f"I am a student with ID: {self.student_id}")

    def study(self):
        print(f"{self.name} is studying.")

# Example usage
if __name__ == "__main__":
    student = Student("Bob", 20, "S12345")
    student.introduce()  # Output: Hello, my name is Bob and I am 20 years old. I am a student with ID: S12345
    student.study()      # Output: Bob is studying.
    print(student.is_adult())  # Output: True
