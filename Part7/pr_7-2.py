import math

arr = [int(input()) for _ in range(5)]
result = 1
for num in arr:
    result *= num
    if math.sqrt(result) == int(math.sqrt(result)):
        print("found")
        break
else:                 # for-else : for 문이 중간에 break 등으로 끊기지 않고, 끝까지 수행 되었을 때 수행 하는 코드
    print("not found")


