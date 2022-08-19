import sys

sys.stdin = open('input.txt')



testNum = int(input())
for test in range(1, testNum+1):
    lst = [list(map(int, input().split())) for i in range(9)]

    ###가로확인
    res = 1
    for row in lst:
        sorted(row)
        cnt = 0
        for a in row:
            cnt +=a

        if cnt != 45:
            res =0
    ##세로확인

    for i in range(9):
        cnt = 0
        for j in range(9):
            cnt += lst[j][i]

        if cnt != 45:
            res =0

    # ##좌하향 대각선 확인.
    # cnt = 0
    # for i in range(9):
    #     cnt += lst[i][i]
    # print(cnt)
    # if cnt != 45:
    #     res =0
    #
    # ##우상향 대각선 확인.
    #
    # cnt =0
    # for i in range(9):
    #     cnt += lst[8-i][i]
    # if cnt != 45:
    #     res =0

    ## 3*3 격자 확인
    #for문 3개
    for i in range(0,7,3):
        for j in range(0,7,3):
            cnt = 0
            for a in range(3):
                for b in range(3):
                    cnt += lst[i+a][j+b]

            if cnt != 45:
                res =0



    print(f'#{test} {res}')