###중간값을 1과 끝값으로 잡아주고
###mid를 그 중간값으로 잡고
##구할 기준을 키워줘야하면 크면 시작을 mid +1
##구할 기준을 줄여 줘야 하면 끝을 mid -1

K, N = map(int, input().split())

lst = [int(input()) for _ in range(K)]

s = 1
e = max(lst)

while s <= e:
    mid = (s+e)//2
    cnt = 0
    for i in lst:
        cnt += i//mid
    if cnt >= N:
        s = mid + 1
    else:
        e = mid - 1
    # print(s,e)
print(e)