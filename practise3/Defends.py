class Animal:
    def speak(self):
        return "ANIMALS CAN SPEAK"
    
class Cat(Animal):
    def speak(self):
        return "MEOW"

class Dog(Animal):
    def speak(self):
        return "ГАВ!"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())