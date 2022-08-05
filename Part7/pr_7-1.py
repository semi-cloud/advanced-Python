# 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴

def solution(mylist):
    return [i * i for i in mylist if i % 2 == 0]

print(solution([3, 2, 6, 7]))
