# i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴

def solution(mylist):
    arr = []
    for num1, num2 in zip(mylist, mylist[1:]):  # 길이가 다른 리스트가 인자로 들어오는 경우, 길이가 짧은 쪽 까지만 이터레이션이 이루어짐
        arr.append(abs(num1 - num2))
    return arr


print(solution([83, 48, 13, 4, 71, 11]))

