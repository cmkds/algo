#A~G  -> 0 ~ 6

adjList =[
    [1 ,2],     # 0
    [0, 3, 5],  # 1
    [0, 4],     # 2
    [1, 5],     # 3
    [1, 2, 5],  # 4
    [3, 4, 6],  # 5
    [5]         # 6
    ]

def dfs(v, N):

    top = -1
    print(v)
    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]:    # if ( v의 인접 정점 중 방문 안한 정점 w가 있으면)
            if visited[w] ==0:
                top += 1        #push(v);
                stack[top] = v
                v = w           # v <- w; (w에 방문)
                visited[w] =1   # visited[w]  <- true;
                print(v)
                break
        else:                   # w가 없으면
            if top != -1:       # 스택이 비어있지 않은 경우
                v = stack[top]  # pop
                top -=1
            else:               # 스택이 비어있으면
                break           # while

# V, E = map(int,input().split())
# N = V +1
# adjList = [[] for _ in range(N)]
# for _ in range(E):
#     a, b = map(int, input().split())
#     adjList[a].append(b)
#     adjList[b].append(a)
N=7
visited = [0] * N   # visited 생성
stack = [0] * N     # stack 생성

dfs(1,N)
print()