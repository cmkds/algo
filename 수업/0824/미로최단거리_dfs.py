def dfs(i, j, N):
    global answer
    if maze[i][j] ==3:
        answer +=1
        return
    else:
        visited[i][j] =1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] !=1 and visited[ni][nj] ==0: #벽으로 둘러쌓인 미로
                dfs(ni,nj,N)
        visited[i][j] = 0
        return




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] ==2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    answer = 0          # 경로의 수
    visited = [[0]*N for _ in range(N)]
    dfs(sti, stj, N)
    print(answer)