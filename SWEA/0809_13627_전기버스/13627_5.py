import sys

sys.stdin = open('input.txt')


def staNum(K,N,M,lst):
    sta = 0 + K
    cnt = 0
    n=0

    while n <= M:
        if sta >= N:
            return cnt

        if sta < lst[cnt]:
            cnt = 0
            return cnt

        for r_sta in lst[:cnt:-1]:
            if sta < lst[0]:
                return 0
            elif lst[0] <= sta < lst[1]:
                sta = lst[0] + K
                cnt += 1
                break
            elif sta >= r_sta:
                sta = r_sta + K

                cnt += 1

        n += 1
    return 0



        # cnt = 0
        # break



testNum = int(input())

for test in range(1, testNum+1):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    # print(K,N,M)
    # print(lst)
    print(f'#{test} {staNum(K,N,M,lst)}')