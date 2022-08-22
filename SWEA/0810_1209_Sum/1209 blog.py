import sys

sys.stdin = open('sum_input.txt')

for test in range(10):

    N = int(input())

    lst = [list(map(int, input().split())) for i in range(100)]

    #최대값을 확인할 변수 생성
    myMax= 0
    tempMax =0

    # 가로값 구하고 최대값과 비교하기 값 100개
    for i in range(100):
        for j in range(100):
            tempMax += lst[i][j]
        if tempMax > myMax:
            myMax = tempMax
        tempMax=0

    #세로값 구하고 최대값과 비교하기  값 100개
    for j in range(100):
        for i in range(100):
            tempMax += lst[i][j]
        if tempMax > myMax:
            myMax = tempMax
        tempMax=0

    #우하향 대각선 구하고 최대값과 비교  값 1개
    for i in range(100):
        tempMax += lst[i][i]

    if tempMax > myMax:
        myMax = tempMax
    tempMax = 0


    #좌상향 대각선 구하고 최대값과 비교  값 1개
    for i in range(100):
        tempMax += lst[99-i][i]

    if tempMax > myMax:
        myMax = tempMax
    tempMax = 0


    print(f'#{N} {myMax}')