import sys

sys.stdin = open('3-4input.txt')

n, m = map(int, input().split())

cnt =0
while n >= m:
    # n이 m으로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % m != 0:
        n -= 1
        cnt += 1
    n //= m
    cnt += 1

while n > 1:
    n -= 1
    cnt +=1


print(cnt)