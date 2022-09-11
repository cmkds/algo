import sys
sys.stdin = open('3-2input.txt')

n, m, k = map(int,input().split())

numLst = list(map(int,input().split()))

numLst.sort(reverse=True)
a = numLst[0]
b = numLst[1]

##가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k + 1)

res = 0
res += count * a
res += (m-count) *b


print(res)
