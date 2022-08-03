# 이차원을 일차원 리스트로 만들기

def solution(mylist):
    result = []
    for element in mylist:
        result += element             # A + B : 배열 A와 B를 연결해 새로운 배열을 리턴
        # result.append(element)      # 배열에 요소 추가 : [['A', 'B'], ['X', 'Y'], ['1']]
    return result

print(solution([['A', 'B'], ['X', 'Y'], ['1']]))