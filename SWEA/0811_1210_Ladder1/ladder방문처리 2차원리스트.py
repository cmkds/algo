import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1]   #오른쪽, 왼쪽, 위쪽
dy = [1, -1, 0]   #오른쪽,왼쪽 위쪽

for _ in range(10):
    case = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]
    n= 100
    y = lst[-1].index(2)
    x = 100 - 1 #99 보는사람을 위해 디테일한 표현하는 방법

    ###방문한 흔적을 남길 행렬을 만들어 놓음
    visited = [[0]*n for _ in range(n)]

    while x != 0:
        visited[x][y] == 1
        for d in range(3):
            nx = x + dx[d]    ##x는 내위치 dx는 갈수있는 방향  nx는 내 미래위치.
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] == 1 and visited[nx][ny] == 0:
                # visited[x][y] == 1
                x = nx
                y = ny

                # 길만 갈게, 방문한 곳 안갈게
                # 1. 길을 지운다.
                    #이동하고 나서 지우기
                    #이동 하기 전에 지우기
                # 2. 방문 표시를 한다. 2-1 리스트  2-2 셋


    print(y)
    #갈수있는곳은 위왼쪽오른쪽
    #순서는 왼쪽오른쪽 먼저 그다음 위쪽