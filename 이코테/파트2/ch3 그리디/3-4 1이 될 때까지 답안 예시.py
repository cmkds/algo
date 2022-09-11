import sys

sys.stdin = open('3-4input.txt')

n, m = map(int, input().split())

cnt =0
while True:
    # n이 m으로 나누어 떨어질 때까지 n에서 1씩 빼기
    target = (n//m) * m
    cnt += (n-target)

    n = target
    #print(target)
    # n이 m 보다 작을 때 (더 이상 나눌 수 없을 때 반복문 탈출)
    if n < m:
        break
    cnt +=1
    n //= m
    #print(n)

cnt += (n-1)
print(cnt)