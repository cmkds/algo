def dfs():
    pass


#정점의 개수, 간선의 개수, 정점의 번호
N, M, V = map(int,input().split())

#
lst = [[] for _ in range(N+1) ]

for i in range(M):
    s, e = map(int, input().split())
    lst[s].append(e)

print(lst)