numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)

words = ["python", "java", "c++"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)

words = ["apple", "banana", "kiwi"]
lengths = list(map(lambda x: len(x), words))
print(lengths)



