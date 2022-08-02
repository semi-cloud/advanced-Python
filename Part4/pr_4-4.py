# 각 원소의 길이를 담은 리스트를 리턴

def solution(mylist):
    return list(map(len, mylist))   # 두 번째 인자의 각 원소에 첫번째 인자로 들어온 함수를 적용

print(solution([[1], [2]]))