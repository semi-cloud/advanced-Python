# 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열 출력

s, n = input().strip().split(' ')
n = int(n)

empty = n - len(s)
print(s + " " * empty)
print(" " * (empty//2) + s + " " * (empty//2))
print(" " * empty + s)
