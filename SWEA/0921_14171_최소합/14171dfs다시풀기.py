import sys
sys.stdin = open('input.txt')

testNum = int(input())

dy = [1, 0]
dx = [0, 1]


def dfs(N,x,y,cnt):
    global res
    if cnt >= res:
        return
    if x==N-1 and y==N-1: #찾은 값에 도달했을 때
        res = cnt
        return
    for i in range(2): #델타탐색리스트의 길이만큼
        nx = x + dx[i]
        ny = y + dy[i]

        if N>nx>=0 and N>ny>=0 and not visited:  #nx, ny가 배열의 범위를 안 벗어날 때만
            visited[y][x] = 1   #방문처리
            dfs(N,nx,ny,cnt+lst[ny][nx])
            visited[y][x] = 0


for test in range(1,1+testNum):
    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    ###dfs(크기,x좌표,y좌표,가면서 계산할 처음 값)

    #이 문제는 0,0 부터 시작
    cnt = lst[0][0]      ##가면서 dfs 깊이의 합을 담을 cnt 변수
    res = 250
    #res의 초기값 이 문제는 최소값을 구하는건데
    #문제에서 가능한 res의 최대값은 25*10 = 250 이다


    dfs(N, 0, 0, cnt)
    print(f'#{test} {res}')
