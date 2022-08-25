import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(start, end, visited):
    q.append(start)
    visited[start] = 0
    while q:
        if visited[end]:
            return visited[end]
        else:
            v = q.popleft()

            for i in lst[v]:        ##해당 노드의 도착점 전부 for문
                if visited[i] ==0:
                    q.append(i)
                    visited[i] = visited[v] +1
            #print(visited)
    return 0




testNum = int(input())

for test in range(1, testNum+1):
    V , E = map(int, input().split())  #V는 노드수 , E는 간선 수

    N = V +1   #### 노드는 1번부터시작하니까 편하게 N+1개로 만들어줌. 0인덱스안쓰려고
    lst =[[] for _ in range(N)]

    q = deque()

    for _ in range(E):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    X, Y = map(int, input().split())  # 출발점, 도착점

    visited = [0] *(N +1)

    a = bfs(X, Y, visited)

    print(f'#{test} {a}')

