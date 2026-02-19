class Dog:
    species = "Canis familiaris"  # Class variable (shared by all dogs)

    def __init__(self, name):
        self.name = name  # Instance variable (unique for each dog)

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)     # Buddy
print(dog2.name)     # Max

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
print(Dog.species)   # Canis familiaris



class Dog:
    species = "Canis familiaris"

dog1 = Dog()
dog2 = Dog()

# Change class variable for all instances
Dog.species = "Modified Species"

print(dog1.species)  # Modified Species
print(dog2.species)  # Modified Species



class Dog:
    species = "Canis familiaris"

dog1 = Dog()
dog2 = Dog()

# Change class variable via object (creates instance variable instead!)
dog1.species = "Dog1 Species"

print(dog1.species)  # Dog1 Species (instance variable)
print(dog2.species)  # Canis familiaris (still class variable)
print(Dog.species)   # Canis familiaris


class Dog:
    count = 0  # Class variable to count dogs

    def __init__(self, name):
        self.name = name
        Dog.count += 1  # Increment class variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Charlie")

print("Number of dogs:", Dog.count)  # 3


class Dog:
    species = "Canis familiaris"

    @classmethod
    def show_species(cls):
        return cls.species

dog = Dog()
print(Dog.show_species())  # Canis familiaris
print(dog.show_species())  # Canis familiaris


