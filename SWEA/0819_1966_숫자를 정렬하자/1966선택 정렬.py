import sys

sys.stdin = open('input.txt')
#선택 정렬  ##버블정렬과 비교하여 이문제에선 큰차이없음

def selectSort(lst):
    for i in range(len(lst)-1):   #### i는 0번부터  1, 2, 3, 4~~~ 채워진다
        tmpMinIdx = i           ###현재값 우측의 최소값을 저장할 minIdx 변수
        for j in range(i+1, len(lst)):  ### 0, 1, 2, 3, 4, 5 ~~~~
            if lst[j] < lst[tmpMinIdx]:    ### lst
                tmpMinIdx = j  ### 우측의 최소값 인덱스를 임시 저장
        lst[i], lst[tmpMinIdx] = lst[tmpMinIdx] , lst[i]  ##첫번째 i에서 가장 최소값 2번째에서 2번째 최소값~~


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    selectSort(lst)

    print(f"#{test} {' '.join(map(str,lst))}")

    ##선택 정렬
