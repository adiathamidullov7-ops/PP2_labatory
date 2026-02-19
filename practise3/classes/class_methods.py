class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Emil", 27)
print(p1.name)
print(p1.age)


class Peron:
    pass
p1 = Person()
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Linus", 28)
print(p1.game)
print(p1.age)


class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age
p1 = Person("Emil")

print(p1.name, p1.age)
