import sys

sys.stdin = open('input.txt')
#합병 병합 정렬
######합병 정렬은 어렵다. 나중에 한번 더 보자. 지금 과한듯
def mergeSort(lst):
    if len(lst) < 2:   #리스트 길이가 2보다 작으면 그대로 내보냄
        return lst
    mid = len(lst) //2      ####리스트 반으로 짜른 값 저장
    lowLst = mergeSort(lst[:mid])    #### 절반 이하 리스트 lowLst 계속 잘리면서 들어간다.
    highLst = mergeSort(lst[mid:])   #### 절반 이상 리스트 highLst

    mergedLst = []       ###새롭게 병합할 리스트 생성
    l = h = 0
    while l < len(lowLst) and h < len(highLst):   ####병한 한것이
        if lowLst[l] < highLst[h]:
            mergedLst.append(lowLst[l])
            l+=1
        else:
            mergedLst.append(highLst[h])
            h+=1
    mergedLst += lowLst[l:]
    mergedLst += highLst[h:]
    return mergedLst


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    a = mergeSort(lst)
    print(f"#{test} {' '.join(map(str,a))}")

    ##병합 정렬
