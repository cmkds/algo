#나무 수 , 가져갈 양

n , m = map(int,input().split())

lst = list(map(int,input().split()))

lst.sort(reverse=True)
k = lst[0]
# print(lst)

cnt = 0
while cnt < m:
    cnt=0
    k -= 1
    for i in lst:
        if i > k:
            cnt += i-k
        else:
            break

print(k)

#####역시 시간초과 날줄 알았다.........