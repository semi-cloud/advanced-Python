# n 진법으로 표기된 문자열을 10진법 숫자로 변환

num, base = map(int, input().strip().split(' '))
result = 0
for idx, n in enumerate(str(num)[::-1]):
    result += int(n) * (base ** idx)
print(result)






