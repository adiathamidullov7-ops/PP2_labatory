def minimal(l):
    min=l[0]
    for i in l:
        if i<min:
           min=i
    return min

def minimal_2(m):
    min2=m[0]
    for i in m:
        if i<min2:
            min2 = i
    return minimal_2
num1 = [1, 2, 3, 4, 5]
min(num1)
num2 = [6, 7, 8, 9]
min(num2)

if num1< num2:
    print("num2")
else:
    print(num2)