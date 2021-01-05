"""
Types of variable in Python:
1. Static variables
2. Instance variables
3. Local variables
"""

class Car:
    wheels = 4 # Static variable
    def __init__(self, mil, com):
        self.mil = mil # self.mil -> Instance, mil -> Local variable.
        self.com = com # self.com -> Instance, com -> Local variable.

c1 = Car(10, 'BMW') # c1, c2 -> Reference variable.
c2 = Car(20, 'Honda')

print(c1.mil, c1.com ,Car.wheels)
print(c2.mil, c2.com ,c2.wheels)
