# for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
#     nx = x + di

#위에다 0 아래에 0 양옆에 0
lst = [[0]+list(map(int,input().split()))+[0] for _ in range(n)]
lst = [[0]*m] + lst + [[0]*m]


