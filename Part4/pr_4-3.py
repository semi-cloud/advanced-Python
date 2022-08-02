# i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴

def solution(mylist):
    arr = []
    for num1, num2 in zip(mylist[:-1], mylist[1:]):  # [ 83, 48, 13, 4, 71, 11] - [ 48, 13, 4, 71, 11]
        arr.append(abs(num1 - num2))
    return arr


print(solution([83, 48, 13, 4, 71, 11]))

