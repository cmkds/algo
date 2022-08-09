import sys

sys.stdin = open('input.txt')

#K =1 move
#N = end station
#M = energy station number
def staNum(K,N,M,lst):
    sta = 0 + K
    cnt = 0
    n=0

    if lst[0] <= sta < lst[1]:
        sta = lst[0] + K
        print('dhodsdf')
        print(sta)
        cnt += 1

    while n <= M:
        if sta >= N:
            return cnt
            break
        print(f'n {n}')
        print(f'cnt {cnt}')
        print(f'lstCnt {lst[cnt]}')
        if sta < lst[cnt]:
            cnt = 0
            return cnt
            break
        for r_sta in lst[:cnt:-1]:
            print(f'sta {sta}')
            print(f'r {r_sta}')
            print(lst[0], lst[1])

            if sta >= r_sta:
                sta = r_sta + K
                print(sta)
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