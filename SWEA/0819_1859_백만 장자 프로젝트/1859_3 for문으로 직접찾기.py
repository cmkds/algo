import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(N-1):
        tmp = 0
        for j in range(i+1,N):
            if lst[j] - lst[i]  > tmp:
                tmp = lst[j] - lst[i]
        cnt += tmp

    print(f'#{test} {cnt}')