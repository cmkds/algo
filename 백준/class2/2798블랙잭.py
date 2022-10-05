N, M = map(int,input().split())
lst = list(map(int,input().split()))

cnt=0
res = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cnt += lst[i]
            cnt += lst[j]
            cnt += lst[k]

            if cnt <= M:
                res.append(cnt)
            cnt = 0
print(max(res))