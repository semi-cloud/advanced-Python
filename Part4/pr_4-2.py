# 2차원 리스트 행과 열 뒤집기
# zip(*iterables) : 각 iterables 의 요소들을 모으는 이터레이터 반환, i번째 튜플은 i번째 원소들 포함(unpacking)

def solution(mylist):
    print(list(map(list, (zip(*mylist)))))    # (1,4,7) (2,5,8) (3,6,9)

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


