# 0이면 영문 소문자 알파벳을, 1이면 영문 대문자 알파벳을 사전 순으로 출력

from string import ascii_lowercase, ascii_uppercase

num = int(input().strip())
print("".join(ascii_lowercase) if num == 0 else "".join(ascii_uppercase))
