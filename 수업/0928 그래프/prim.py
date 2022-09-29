


###### prim #######################################################################################

'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from collections import defaultdict

V, E = map(int,input().split())
graph_list = defaultdict(list)
graph_matrix = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, weight = map(int,input().split())
    graph_list[s].append((weight,s,e))
    graph_list[e].append((weight,e,s))

    graph_matrix[s][e] = weight
    graph_matrix[e][s] = weight

print(graph_list)
print(graph_matrix)
# defaultdict(<class 'list'>, {0: [(32, 0, 1), (31, 0, 2), (60, 0, 5), (51, 0, 6)], 1: [(32, 1, 0), (21, 1, 2)], 2: [(31, 2, 0), (21, 2, 1), (46, 2, 4), (25, 2, 6)], 5: [(60, 5, 0), (18, 5, 3), (40, 5, 4)], 6: [(51, 6, 0), (25, 6, 2), (51, 6, 4)], 4: [(46, 4, 2), (34, 4, 3), (40, 4, 5), (51, 4, 6)], 3: [(34, 3, 4), (18, 3, 5)]})
# [[0, 32, 31, 0, 0, 60, 51], [32, 0, 21, 0, 0, 0, 0], [31, 21, 0, 0, 46, 0, 25], [0, 0, 0, 0, 34, 18, 0], [0, 0, 46, 34, 0, 40, 51], [60, 0, 0, 18, 40, 0, 0], [51, 0, 25, 0, 51, 0, 0]]

# prim

def prim(node):
    mst = [0]*(V+1)
    key = [float('inf')]*(V+1)
    parent = [-1]*(V+1)  ##내 부모노드를 찾는 역할.
    key[node] = 0
    for _ in range(V+1):
        min_val = float('inf')

        for i in range(V+1):
            if mst[i]==0 and key[i] < min_val:
                s = i
                min_val = key[i]
        mst[s] = 1

        for e in range(V+1):
            if mst[e] == 0 and graph_matrix[s][e]>0:
                if key[e] > graph_matrix[s][e]:
                    key[e] = graph_matrix[s][e]
                    parent[e] = s
    return sum(key)






# prim, 우선순위 큐


import heapq

def prim2(node):
    
    mst = []

    visited = {node}

    candidate = graph_list[node]
    heapq.heapify(candidate)

    while len(visited) < V and candidate :
        weight, s, e = heapq.heappop(candidate)

        if e not in visited:
            visited.add(e)
            mst.append((weight,s,e))

            for route in graph_list[e]:
                if route[2] not in visited:
                    heapq.heappush(candidate, route)

    return sum(map(lambda x : x[0], mst))