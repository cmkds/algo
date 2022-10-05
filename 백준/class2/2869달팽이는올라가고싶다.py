import math
A, B, V = map(int,input().split())

cnt = 1
C = A-B

cnt += math.ceil((V-A)/(A-B))

print(cnt)