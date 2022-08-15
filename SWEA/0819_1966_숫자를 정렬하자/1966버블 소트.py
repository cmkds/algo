import sys

sys.stdin = open('input.txt')
#버블 정렬

def bubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1] , lst[j]


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    bubbleSort(lst)

    print(f"#{test} {' '.join(map(str,lst))}")

    ##버블 정렬
