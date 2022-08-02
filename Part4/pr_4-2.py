# 2차원 리스트 행과 열 뒤집기

def solution(mylist):
    n = len(mylist)
    answer = [[0] * n for _ in range(n)]
    for i, row in enumerate(mylist):
        for j, num in enumerate(row):
            answer[j][i] = num
    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

