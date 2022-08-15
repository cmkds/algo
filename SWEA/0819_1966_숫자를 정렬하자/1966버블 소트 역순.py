import sys

sys.stdin = open('input.txt')
#버블 정렬 역순
def bubbleSortReverse(lst):
    for i in range(len(lst)-1, 0, -1): # 4 3 2 1
        for j in range(len(lst)-1, len(lst)-i-1 , -1):   # 4 3 2 1  432 43 4 (0 1 2 3
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1] , lst[j]


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    bubbleSortReverse(lst)

    print(f"#{test} {' '.join(map(str,lst))}")

    ##버블 정렬 역순
