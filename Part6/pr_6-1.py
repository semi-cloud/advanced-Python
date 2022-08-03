# 이차원을 일차원 리스트로 만들기

import itertools
from functools import reduce
import operator
# reduce : 반복 가능한 객체(iterable object) 내 각 요소를 연산한 뒤 이전 연산 결과들과 누적해서 반환

def solution(mylist):
    # 방법 1 : sum
    result = sum(mylist, [])

    # 방법 2 - itertools.chain
    result = list(itertools.chain.from_iterable(mylist))

    # 방법 3 - itertools unpacking
    result = list(itertools.chain(*mylist))

    # 방법 4 - list comprehension 이용
    result = [element for array in mylist for element in array]

    # 방법 5 - reduce 함수 이용 1
    result = list(reduce(lambda x, y: x + y, mylist))

    # 방법 6 - reduce 함수 이용 2
    result = list(reduce(operator.add, mylist))

    return result


print(solution([['A', 'B'], ['X', 'Y'], ['1']]))