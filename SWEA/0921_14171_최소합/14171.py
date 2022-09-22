import sys
sys.stdin = open('input.txt')


testNum = int(input())

def dfs(N, y, x, cnt):
    global res
    if y == N-1 and x == N-1:
        if cnt < res:
            res = cnt
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs(N,ny,nx,cnt+lst[ny][nx])
            visited[ny][nx] = 0



dy = [1, 0]
dx = [0, 1]

for test in range(1,1+testNum):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    cnt = lst[0][0]

    res = sum(lst[0])
    for i in range(1,N):
        res += lst[i][-1]

    visited[0][0] = 1
    dfs(N,0,0,cnt)

    print(f'#{test} {res}')


