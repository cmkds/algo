import sys
sys.stdin = open('4-1.txt')

#공간을 벗어나는 움직임은 무시된다.
n = int(input())
x, y = 1, 1
go = input().split()
print(go)

#델타탐색
dx=[0,0,-1,1]
dy=[-1,1,0,0]
lst = ['L','R','U','D']

for g in go:
    for i in range(4):
        if g == lst[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)