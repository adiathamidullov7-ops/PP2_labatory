class Animal():
    def speak(self):
        return "Animals can speak"

class Dog(Animal):
    def speak(self):
        return super().speak() + "and laugh"
dog = Dog()
print(dog.speak())

# Parent class Father
class Father:
    def skills(self):
        return "Repair"  # Father has repair skills

# Parent class Mother
class Mother:
    def skills(self):
        return "Cooking"  # Mother has cooking skills

# Child class inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        # Call the method from the first parent in MRO and add extra skill
        return super().skills() + " and Sports"

# Create an in


class Father:
    def skills(self):
        return "Ремонт"

class Mother:
    def skills(self):
        return "Готовка"

class Child(Father, Mother):
    def skills(self):
        return super().skills() + " и спорт"

child = Child()
print(child.skills())  # "Ремонт и спорт"



class Vehicle:
    def start(self):
        return "Машина заводится"

class Car(Vehicle):
    def start(self):
        original = super().start()  # вызываем метод родителя
        return original + " и готова к поездке"

car = Car()
print(car.start())  # "Машина заводится и готова к поездке"
