class Dog:
    species = "Canis familiaris"  # Class variable (общая для всех объектов)

    def __init__(self, name, age):
        self.name = name  # Instance variable (уникальна для каждого объекта)
        self.age = age    # Instance variable

# Создаём объекты
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name, dog1.age, dog1.species)  # Buddy 3 Canis familiaris
print(dog2.name, dog2.age, dog2.species)  # Max 5 Canis familiaris



class Dog:
    count = 0  # Class variable для подсчёта объектов

    def __init__(self, name):
        self.name = name  # Instance variable
        Dog.count += 1    # Увеличиваем class variable при создании объекта

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Charlie")

print("Number of dogs:", Dog.count)  # 3



class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_species(cls):
        return cls.species

dog = Dog("Buddy")
print(dog.show_species())  # Canis familiaris
print(Dog.show_species())  # Canis familiaris


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, species=None):
        self.name = name
        if species:
            Dog.species = species  # Изменяем class variable через init

dog1 = Dog("Buddy", "Modified Species")
dog2 = Dog("Max")

print(dog1.name, dog1.species)  # Buddy Modified Species
print(dog2.name, dog2.species)  # Max Modified Species


