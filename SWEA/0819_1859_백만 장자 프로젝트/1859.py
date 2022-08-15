import sys

sys.stdin = open('input.txt')
#############pop을쓰니가 짧고 효율적인데 시간 초과가 뜬다.

testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))

    #맨앞에껄 pop으로 빼고
    #뒤로가면서 가장큰 차액이 있으면
    #그 차액 만큼 더한다.
    cnt = 0
    while 1:
        tmp = lst.pop(0)
        if not lst:
            break
        if tmp < max(lst):
            cnt += max(lst)-tmp

    print(f'#{test} {cnt}')