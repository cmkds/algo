from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, E = map(int, input().split())

    adj = [[11 * (N + 1)] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adj[i][i] = 0

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    print(adj)
    res_lst = [0] + [11 * (N + 1)] * (N)

    q = deque([0])
    while q:
        start = q.popleft()
        for i in range(N + 1):
            if i != start and 0 < res_lst[start] + adj[start][i] < res_lst[i]:
                if res_lst[start] + adj[start][i] < res_lst[i]:
                    res_lst[i] = res_lst[start] + adj[start][i]
                if i != N:
                    q.append(i)

    print(f'#{case + 1} {res_lst[N]}')