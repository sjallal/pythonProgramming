"""
Types of methods in Python are:
1. Instance methods : If you wanna work with instance variables.
2. Class methods : If you wanna work with class variables.
3. Static methods : If you don't wanna work with any of the variables.
"""


class Student:
    # Class variables
    school = "Saqib's University"

    # Constructor
    def __init__(self, m1, m2, m3):
        # Instance Variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Methods
    def get_avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Class Methods
    @classmethod
    def get_school(cls):
        return cls.school

    # Static Methods
    @staticmethod
    def info():
        print("This is a student class...")


if __name__ == "__main__":
    s1 = Student(2, 3, 4)
    s2 = Student(1, 5, 2)

    print(s1.get_avg())
    print(s2.get_avg())

    print(Student.get_school())

    Student.info()
