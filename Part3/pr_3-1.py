# 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열 출력

s, n = input().strip().split(' ')
n = int(n)

s.ljust(n)         # 좌측 정렬
s.center(n)       # 가운데 정렬
s.rjust(n)        # 우측 정렬
