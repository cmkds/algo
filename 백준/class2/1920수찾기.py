##set으로 탐색 하는것이 리스트 탐색보다 속도가 훨씬 빠르다

n = int(input())
lst = sorted(list(map(int,input().split())))

m = int(input())
chkLst = list(map(int,input().split()))

##인덱스로 탐색
def binary(i):
    s = 0
    e = n-1

    while s <= e:
        mid = (s+e)//2
        if lst[mid] == i:
            return 1
        if i<lst[mid]:
            e = mid-1
        else:
            s = mid+1

for i in chkLst:
    if binary(i):
        print(1)
    else:
        print(0)