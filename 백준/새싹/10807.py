n = int(input())
lst = list(map(int,input().split()))
chk = int(input())

cnt = 0
for a in lst:
    if a ==chk:
        cnt +=1
print(cnt)