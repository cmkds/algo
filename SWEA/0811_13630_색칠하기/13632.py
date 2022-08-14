import sys

sys.stdin = open('input.txt')


testNum = int(input())


##빨간색 1 파란색 2
for test in range(1, testNum+1):
    ncolor = int(input())

    #10*10  [0] 리스트 초기화화
    lst= [[0]*10 for _ in range(10)]

    for _ in range(ncolor):
        x1, y1, x2, y2, color = map(int, input().split())

        #빨간색 찍기
        if color ==1:
            for x in range(x1,x2+1):
                for y in range(y1, y2+1):
                    if lst[x][y] == 0:
                        lst[x][y] = 1
                    elif lst[x][y] == 2:
                        lst[x][y] = 3
        #파란색 찍기
        if color ==2:
            for x in range(x1,x2+1):
                for y in range(y1, y2+1):
                    if lst[x][y] == 0:
                        lst[x][y] = 2
                    elif lst[x][y] == 1:
                        lst[x][y] = 3

    #리스트중에 3인컷 카운트하기
    cnt = 0
    for x in range(10):
        for y in range(10):
            if lst[x][y] == 3:
                cnt +=1
    print(f'#{test} {cnt}')
