import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 그래프 표현
    mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for s, e, w in edges:
        mat[s][e] = w
    print(mat)