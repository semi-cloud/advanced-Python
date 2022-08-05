import math

arr = [int(input()) for _ in range(5)]
result = 1
flag = False
for num in arr:
    result *= num
    if math.sqrt(result) == int(math.sqrt(result)):
        flag = True
        print("found")
        break

if not flag:
    print("not found")


