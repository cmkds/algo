N, M = map(int,input().split())
lst = list(map(int,input().split()))

res = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cnt = lst[i] + lst[j] + lst[k]

            if cnt <= M:
                res = max(res, cnt)
            cnt = 0
print(res)