import sys

sys.stdin = open('3-4input.txt')

n, m = map(int, input().split())

cnt =0
while n != 1:
    if n % m ==0:
        n /= m
        cnt += 1
        continue
    else:
        n-= 1
        cnt +=1
print(cnt)