class Animal:
    def speak(self):
        return "Sound"
class Cat(Animal):
    def speak(self):
        return "MEOW"
print(Cat.speak())





class Grandparent:
    def house(ielf):
        return "Big House"

class Parent(Grandparent):
    def car(ielf):
        return "a Car"
class Child(Parent):
    def phone(ielf):
        return "Phone"
child = Child()
print(child.house())
print(child.car)
print(child.phone())



class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"Имя: {self.name}"

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def info(self):
        return f"{super().info()}, Класс: {self.grade}"

student = Student("Ali", 10)
print(student.info())


class Animal():
    def speak(myself):
        return "Animals can speak"

class Dog(Animal):
    def bark(myself):
        return "Goofy"
dog= Dog()
print(dog.speak())
print(dog.bark())


