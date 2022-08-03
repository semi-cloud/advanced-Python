# 배열의 원소로 이루어진 모든 순열을 사전순으로 리턴

from itertools import permutations

def solution(mylist):
    return sorted(list(map(list, permutations(mylist, len(mylist)))))  # 사전순 자동 정렬

print(solution([1, 2, 3]))
