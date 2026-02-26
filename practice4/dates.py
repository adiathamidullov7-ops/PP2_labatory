mytyple = ("apple", "banana", "cherry")
my = iter(mytyple)

print(next(my))
print(next(my))
print(next(my))



mystr = "banana"
for x in mystr:
    print(x)


class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myClass = Numbers()
myiter = iter(myClass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))