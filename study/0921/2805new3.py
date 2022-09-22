import sys
input = sys.stdin.readline

n , m = map(int,input().split())

lst = list(map(int,input().split()))

lst.sort()
k = lst[-1]


cnt = 0
dumi = 0
while cnt < m:
    k -=1
    for i in reversed(lst):
        if i > k:
            del lst[-1]
            dumi +=1
        else:
            break
    cnt += dumi

print(k)

