import sys
sys.stdin = open('3-2input.txt')

n, m, k = map(int,input().split())

numLst = list(map(int,input().split()))

numLst.sort(reverse=True)
a = numLst[0]
b = numLst[1]

res = 0
### n은 안중요  m는 더하는 횟수 k는 한번에 최대 더하는 수.
###
while m != 0:
    for i in range(k):
        if m== 0:
            break
        res += a
        m -= 1
    if m==0:
        break
    res += b
    m -= 1
print(res)
