#나무 수 , 가져갈 양

n , m = map(int,input().split())

lst = list(map(int,input().split()))

lst.sort()
k = lst[-1]
# print(lst)

cnt = 0
dumi = 0
while cnt < m:
    k -=1
    for i in reversed(lst):
        if i > k:
            lst.pop()
            dumi +=1
        else:
            break
    cnt += dumi
    # print(cnt, dumi)

print(k)

#####역시 시간초과 날줄 알았다.........