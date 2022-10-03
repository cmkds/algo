K, N = map(int, input().split())

lst = [int(input()) for _ in range(K)]

s = 1
e = max(lst)

while(s <= e):
    mid = (s+e) // 2
    cnt = 0
    for i in lst:
        cnt += i//mid
    if cnt >= N:
        s = mid + 1
    else:
        e = mid -1
print(e)