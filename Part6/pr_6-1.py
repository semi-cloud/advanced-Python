# 이차원을 일차원 리스트로 만들기

def solution(mylist):
    result = []
    for lis in mylist:
        for num in lis:
            result.append(num)
    return result

print(solution([['A', 'B'], ['X', 'Y'], ['1']]))