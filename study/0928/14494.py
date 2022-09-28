n,m = map(int,input().split())

lst = [[0]*m for _ in range(n)]

for i in range(n):
    lst[i][0] = 1
for i in range(m):
    lst[0][i] = 1


for i in range(n):
    for j in range(m):
        if not lst[i][j]:
            lst[i][j] = lst[i-1][j]+ lst[i][j-1] + lst[i-1][j-1]

print(lst[n-1][m-1] % 1000000007)