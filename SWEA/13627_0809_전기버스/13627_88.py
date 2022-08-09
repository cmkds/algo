import sys

sys.stdin = open('input.txt')

def staNum(K,N,M,lst):
    sta = K
    cnt = 0
    n = 0
    k = 0

    if sta < lst[0]:
        return 0
    if lst[0] <= sta < lst[1]:
        sta = lst[0] + K
        cnt += 1
        k = 1

    while n <= M:
        if sta >= N:
            return cnt

        for r_sta in lst[:cnt:-1]:

            if sta >= r_sta:
                sta = r_sta + K
                cnt += 1

        n += 1
    if k == 1:
        if sta < lst[cnt]:
            return 0
    elif k == 0:
        if sta < lst[cnt + 1]:
            return 0




testNum = int(input())

for test in range(1, testNum+1):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))


    print(f'#{test} {staNum(K,N,M,lst)}')