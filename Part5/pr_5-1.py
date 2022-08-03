# 리스트의 원소를 모두 이어붙인 문자열을 리턴

def solution(mylist):
    str = ""
    for num in mylist:
        str += num
    return str

solution(['1', '100', '33'])
