def show_the_person(name, surname):
    return name + " " + surname
result = show_the_person("Jeffrey" + "Epstein")
print(result)

def print_numbers(n):
    for i in range(n):
        print(i)

print_numbers(5)


def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to_n(5))

def get_even_numbers(n):
    evens = []
    for i in range(n):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(get_even_numbers(10))
