import sys

sys.stdin = open('input.txt')

def dfs(X):
    visited[X] = 1
    for X in lst[X]:
        if visited[X] == 0:
            dfs(X)



testNum = int(input())

for test in range(1, testNum+1):
    V , E = map(int, input().split())  #V는 노드수 , E는 간선 수

    N = V + 1   #### 노드는 1번부터시작하니까 편하게 N+1개로 만들어줌. 0인덱스안쓰려고
    lst =[[] for _ in range(N)]

    #E개줄만큼 간선이 주어짐
    for _ in range(E):
        a, b = map(int, input().split())
        lst[a].append(b)
        #lst[b].append(a) #한방향만 되는거냐??? 아주친절하네

    X, Y = map(int, input().split()) #출발점, 도착점

    visited = [0] * N

    dfs(X)
    print(visited)
    print(f'#{test} {visited[Y]}')


