import sys
sys.stdin = open('1.txt')

n = int(input())
lst = list(map(int,input().split()))

lst.sort(reverse=True)

cnt = 0
tmpCnt = 0
while lst:
    a = lst.pop()
    tmpCnt +=1
    if tmpCnt >= a:
        tmpCnt =0
        cnt += 1
print(cnt)