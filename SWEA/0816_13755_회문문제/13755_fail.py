import sys

sys.stdin = open('input.txt')

testNum = int(input())


for test in range(1, testNum + 1):
    N, M = map(int, input().split())

    lst = [list(input()) for i in range(N)]

    for l in lst:
        for r in range(N - M + 1):
            chk = 0
            for m in range(M//2):

                if l[r + m] == l[M - 1 - m + r]:
                    chk += 1
                else:
                    chk = 0

                if chk == (M // 2):
                    res = ''
                    for k in range(M):
                        res = res + l[r + m - (M // 2) + 1 + k]

    lst = list(zip(*lst))
    for l in lst:

        for r in range(N - M + 1):
            chk = 0
            for m in range(M//2):
                if l[r + m] == l[M - 1 - m + r]:
                    chk += 1
                else:
                    chk = 0

                if chk == (M // 2):
                    res = ''
                    for k in range(M):
                        res = res + l[r + m - (M // 2) + 1 + k]

    print(f'#{test} {res}')