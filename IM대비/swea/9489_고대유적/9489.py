import sys

sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1,testNum+1):
    N, M = map(int,input().split())

    lst = [list(map(int,input().split())) for _ in range(M)]
    print(lst)
    cntGaro = 0
    cntSero = 0
    maxCnt = 0
    for i in range(N):
        for j in range(M):
            ##가로
            if lst[i][j] ==1:
                cntGaro +=1
            else:
                if maxCnt < cntGaro:
                    maxCnt = cntGaro
                cntGaro = 0
            ##가로
            if lst[j][i] ==1:
                cntSero +=1
            else:
                if maxCnt < cntSero:
                    maxCnt = cntSero
                cntSero = 0
