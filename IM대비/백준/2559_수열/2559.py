import sys

sys.stdin = open('input.txt')


N , chkN = map(int,input().split())
lst = list(map(int,input().split()))

tmpSum = sum(lst[:chkN])
#res = -10000000    ##이렇게 했더니 N과 chkN이 같을 때 오류뜸
res = sum(lst[:chkN])    #그래서 이렇게 함

for i in range(1,N-chkN+1):
    tmpSum = tmpSum - lst[i-1] + lst[i+chkN-1]

    res = max(res, tmpSum)   ##이게 조금 오래걸림
    # if tmpSum > res:
    #     res = tmpSum

print(res)