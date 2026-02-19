class Vehicle:
    def start(self):
        return "Car starting"

class Car(Vehicle):
    def start(self):
        original = super().start()
        return original + "and ready to go"

car = Car()
print(car.start()) 


class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

cat = Cat("NALA", "WHITE")
print(cat.name)  
print(cat.color)


class Person:
    def info(self):
        return "a man"

class Student(Person):
    def info(self):
        return super().info() + "Student"

student = Student()
print(student.info()) 



class Animal:
    def speak(self):
        return "ANIMALS CAN SPEAK"

class Dog(Animal):
    def speak(self):
        return "AHAHAAHA"

dog = Dog()
print(dog.speak())