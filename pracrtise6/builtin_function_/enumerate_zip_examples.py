names = ["Jake", "Jeffrey", "Jesse"]
scores = [85, 90, 78]

for index, name in enumerate(names):
    print(index, name)

for name, score in zip(names, scores):
    print(name, score)

nums = [5, 2, 9, 1]
print("Sorted numbers:", sorted(nums))

num = "10"
converted = int(num)
print(type(converted), converted)