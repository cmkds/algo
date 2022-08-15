import sys

sys.stdin = open('input.txt')
#힙 정렬은 영상을 봐도 감이 잘 안온다???? 병합은 대충 감이라도 왔는데
#이건 어디가 효율적인걸까..
#코드를 봐도 동영상에서 움직였던거 감만 잡히는 정도

def heapSort(lst):
    n = len(lst)
    for i in range(n):  ##배열 길이 만큼 돌린다.
        c = i
        while c != 0:
            r = (c-1)//2
            if (lst[r]< lst[c]):
                lst[r], lst[c] = lst[c], lst[r]
            c = r
     #       print(lst)
    #크기를 줄여 가면서 heap 구성
    for j in range(n-1, -1, -1):
        lst[0], lst[j] = lst[j] , lst[0]
        r = 0
        c = 1
        while c < j:
            c = 2*r +1
            #자식 중 더 큰 값 찾기
            if (c < j-1) and (lst[c] < lst[c+1]):
                c += 1
            # 루트 보다 자식이 크다면 교환
            if (c < j) and (lst[r] < lst[c]):
                lst[r], lst[c] = lst[c] , lst[r]
            r = c



testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    heapSort(lst)

    print(f"#{test} {' '.join(map(str,lst))}")

    ##힙 정렬
