import json

x = '{name: "John", "age":30, "city":"New York"}'
y = json.load(x)
print(y["age"])



import json

x = {
    "name": "John",
    "age": "New York"
}
y = json.dumps(x)
print(y)

import json

print(json.dumps({"banana" , "apple", "pinapple"}))
print(json.dumps("age: 30"))
print(json.dumps("hello"))


import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW M5 F90", "mpg": 27.5}
        {"model": "Ford Mustang Shelby", "mpg": 24.1}

    ]

}
print(json.dumps(x))