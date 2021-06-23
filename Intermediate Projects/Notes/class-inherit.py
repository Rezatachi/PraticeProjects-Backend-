# Class inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        # A super refers to the super class. Basically intializeing everything you can do with the super class. In this case the Animal class is called and all of its inits are utilized
        super().__init__()

    def breathe(self):
        super().breathe()
        print("You can do this underwater")

    def swim(self):
        print("You can swim!")


nemo = Fish()
nemo.breathe()
