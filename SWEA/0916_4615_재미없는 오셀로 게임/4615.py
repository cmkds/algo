import sys
sys.stdin = open('input.txt')

###돌을 놓으면 그곳을 기준으로 상하좌우 대각선탐색
###다른번호부터 원래 내번호가 되는 경우
###그 사이의 다른번호를 내번호로 바꾸기

dx = [0,0,-1,1,-1,-1,1,1]
dy = [-1,1,0,0,-1,1,-1,1]


testNum = int(input())
for test in range(1,1+testNum):
    N, M = map(int,input().split())
    lst = [[0]*N for _ in range(N)]

    ###기본 배치하기 흑돌 1 백돌 2
    lst[N//2-1][N//2-1] = 2
    lst[N // 2 - 1][N // 2 ] = 1
    lst[N // 2 ][N // 2 - 1] = 1
    lst[N // 2][N // 2] = 2

    for _ in range(M):
        y, x, k = map(int,input().split())

    ##8방향 탐색
        for i in range(8):
            ny = y - 1   ## -1은 인덱스로 탐색하기 위함
            nx = x - 1
            cnt = 1      ##같은 숫자를 만났을 때 사용할 변수

            while 0 <= nx+dx[i] <N and 0 <= ny+dy[i] < N and lst[ny+dy[i]][nx+dx[i]]:
                ##같은 숫자일 경우
                if lst[ny+dy[i]][nx+dx[i]] == k:
                    for a in range(cnt):
                        lst[y-1+dy[i]*a][x-1+dx[i]*a] = k
                    break

                ##다른 숫자일 경우
                else:
                    ny += dy[i]
                    nx += dx[i]
                    cnt += 1

    cnt1,cnt2=0,0
    for i in range(N):
        for j in range(N):
            if lst[i][j]==1:
                cnt1 +=1
            elif lst[i][j]==2:
                cnt2 +=1

    print(f'#{test} {cnt1} {cnt2}')


