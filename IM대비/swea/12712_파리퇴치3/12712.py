import sys
sys.stdin = open('input.txt')

dy1 = [0, 1, 0, -1]     #+모양
dx1 = [1, 0, -1, 0]
dy2 = [1, 1, -1, -1]    #x 모양
dx2 = [1, -1, -1, 1]

TestNum = int(input())

for test in range(1, TestNum+1):
    N, M = map(int,input().split())

    lst = [list(map(int,input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        for j in range(N):
            cnt = lst[i][j]  #i, j를 중심으로 + 모양

            for k in range(4):
                for m in range(1,M):
                    nx=i+dx1[k]*m
                    ny=j+dy1[k]*m
                    if 0<=nx<N and 0<=ny<N:
                        cnt += lst[nx][ny]
            #print(cnt)
            if cnt >= res:
                res= cnt

    for i in range(N):
        for j in range(N):
            cnt = lst[i][j]  #i, j를 중심으로 + 모양

            for k in range(4):
                for m in range(1,M):
                    nx=i+dx2[k]*m
                    ny=j+dy2[k]*m
                    if 0<=nx<N and 0<=ny<N:
                        cnt += lst[nx][ny]
           # print(cnt)
            if cnt >= res:
                res = cnt

    print(f'#{test} {res}')