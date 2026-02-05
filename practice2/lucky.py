n = int(input())
arr = list(map(int, input().split()))

arr.sort()  

count = 1
max_count = 1
number = arr[0]

for i in range(1, n):
    if arr[i] == arr[i - 1]:
        count += 1
    else:
        count = 1  

   
        max_count = count
        number = arr[i]

print(number)
