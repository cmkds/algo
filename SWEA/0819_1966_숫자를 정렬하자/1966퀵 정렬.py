import sys

sys.stdin = open('input.txt')
# 퀵 정렬 실행시간 제일 빠른듯?

def quickSort(lst, start, end):  ##start 는 0   end 는 리스트 길이 -1
    if start >= end:
        return
    pivot = start   ##피벗은 첫번째 원소로 지정
    left = start +1  ## 좁혀지는 왼쪽 값
    right = end      ### 좁혀지는 오른쪽 값
    while(left <= right):
        #피벗 보다 큰 데이터를 찾을 때 까지 반복
        while(left <= end and lst[left] <= lst[pivot]):
            left += 1
        #피벗 보다 작은 데이터를 찾을 때 까지 반복
        while(right > start and lst[right] >= lst[pivot]):
            right -= 1
        if(left> right):  #만약 엇갈렸다면 작은 데이터와 피벗을 교체 ???????????????????
            lst[right] , lst[pivot] = lst[pivot], lst[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체     ?????????
            lst[left], lst[right] = lst[right], lst[left]

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(lst, start, right-1)
    quickSort(lst, right+1, end)


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    quickSort(lst, 0, len(lst)-1)

    print(f"#{test} {' '.join(map(str,lst))}")

    ##퀵 정렬
