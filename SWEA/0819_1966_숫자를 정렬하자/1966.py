import sys

sys.stdin = open('input.txt')

def bubbleSortReverse(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1] , lst[j]

def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1] , lst[j]


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(str, input().split()))  #숫자리스트 str값으로 받음
    bubbleSort(lst)
    # print(lst) #이 리스트를 정렬 해야함
    print(f"#{test} {' '.join(lst)}")

    ##버블 정렬
