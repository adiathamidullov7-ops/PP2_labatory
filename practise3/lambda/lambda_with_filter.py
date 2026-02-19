numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

numbers = [-5, 3, -1, 7, -8, 2]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)

words = ["cat", "elephant", "dog", "giraffe"]
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)

numbers = [5, 12, 7, 18, 3, 20]
big_numbers = list(filter(lambda x: x > 10, numbers))
print(big_numbers)



