import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(N-1):
        tmp = 0
        if max(lst[i+1:N]) - lst[i] > tmp:
            tmp = max(lst[i+1:N]) - lst[i]
        cnt += tmp

    print(f'#{test} {cnt}')