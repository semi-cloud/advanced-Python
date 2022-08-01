# base 진법으로 표기된 숫자를 10진법 숫자 출력 하기

num, base = map(int, input().strip().split(' '))
num = str(num)
result, j = 0, 0
for i in range(len(num) - 1, -1, -1):
    result += int(num[i]) * (base ** j)
    j += 1
print(result)






