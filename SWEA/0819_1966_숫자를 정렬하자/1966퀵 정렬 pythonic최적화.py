import sys

sys.stdin = open('input.txt')
# 퀵 정렬 실행시간 제일 빠른듯?
# 퀵정렬 pythonic 최적화 코드

def quickSort(lst):
    #리스트 원소가 한개 이하 인경우
    if len(lst) <=1:
        return lst
    pivot = lst[0] # 피벗은 리스트 첫번째 원소로 지정
    tail = lst[1:]  # 피벗을 제외한 리스트

    leftSide = [x for x in tail if x<= pivot]  #분할된 왼쪽 부분
    rightSide = [x for x in tail if x> pivot]  #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quickSort(leftSide) + [pivot] + quickSort(rightSide)


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    a = quickSort(lst)

    print(f"#{test} {' '.join(map(str,a))}")

    ##퀵 정렬
