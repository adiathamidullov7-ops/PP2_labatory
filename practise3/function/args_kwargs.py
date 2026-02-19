def my_kids(*kids):  #Creating function "Whose my kid?"
    print("My kid " + kids[0] ) #Chossing my kid
my_kids("Alisa", "Maria", "Kane") #The Set of my kid

def my_kids_2(*args):
    print("Type: ",  type(args))
    print("First argument: ", args[0])
    print("Second argument: ", args[1] )
    print("All arguments: ", args)
my_kids_2("Alisa", "Maria", "Kane")

def my_kids_3(greeting, *names):
    for name in names:
        print(greeting, name)
my_kids_3("Hello ", "Maria", "Kane")

def my_function(*number):
    total = 0
    for num in number:
        total += num
    return total
print(my_function(1,2,3))
print(my_function(10, 20, 30, 40))
print(my_function(5))