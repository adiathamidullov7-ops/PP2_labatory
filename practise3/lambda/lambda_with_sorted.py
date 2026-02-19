numbers = [4, 1, 7, 3, 9]
result = sorted(numbers, key=lambda x: x, reverse=True)
print(result)

words = ["python", "java", "c", "javascript"]
result = sorted(words, key=lambda x: len(x))
print(result)

words = ["cat", "dog", "tiger", "elephant"]
result = sorted(words, key=lambda x: x[-1])
print(result)

people = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 19},
    {"name": "John", "age": 30}
]

result = sorted(people, key=lambda x: x["age"])
print(result)






