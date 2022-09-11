import sys

sys.stdin = open('5.txt')

n, m = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0
for i in range(len(lst)-1):
    for j in range(1,len(lst)):
        if i>=j:
            continue
        elif lst[i]==lst[j]:
            continue
        else:
           # print((i+1,j+1))
            cnt += 1
print(cnt)