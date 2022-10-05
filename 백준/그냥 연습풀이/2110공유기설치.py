import sys
input = sys.stdin.readline

n, c = map(int,input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()

s = 1
e = lst[-1]

res = 0

while s <= e:
    mid = (s+e)//2
    cnt = 1
    chk = lst[0]
    for i in range(1, n):
        if lst[i] >= chk+mid:
            cnt +=1
            chk = lst[i]
    if cnt >= c:
        s = mid +1
        res = mid
    else:
        e = mid -1
    # print(chk,mid)
    # print(res)
print(res)