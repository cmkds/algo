import sys

sys.stdin = open('input.txt')

def staNum(K,N,M,lst):
    sta = K
    cnt = 0
    n=0

    # 밑에 for문에 0 까지 안들어가서 0 ,1 사이인 경우는 따로 빼줌.
    if lst[0] <= sta < lst[1]:
        sta = lst[0] + K
        cnt = 1

        while n <= 100:
        # 이게 아니고 while True? 아니야 이건 의미 없어
        # while True:
            #스테이션이 종점에 도착했다면 cnt를 리턴한다.
            if sta >= N:
                return cnt
            #lst를 거꾸로 돌리면서 이동가능한 가장먼 정거장(r_sta)이 있을때
            #r_sta로 이동후 K최대 이동거리만큼 이동하고 충전 카운트를 올린다.
            for r_sta in lst[:cnt:-1]:

                if sta >= r_sta:
                    sta = r_sta + K
                    cnt += 1
            #현재 위치가 다음 정거장을 못넘으면 작다면 0을 리턴한다
            print('sta', end='')
            print(sta)
            print('lst', end='')
            print(lst[cnt])
            print(cnt)
            if sta < lst[cnt]:
                return 0

            n += 1

    else:
        while n <= 100:
        # 이게 아니고 while True? 아니야 이건 의미 없어
        # while True:
            #스테이션이 종점에 도착했다면 cnt를 리턴한다.
            if sta >= N:
                return cnt
            #lst를 거꾸로 돌리면서 이동가능한 가장먼 정거장(r_sta)이 있을때
            #r_sta로 이동후 K최대 이동거리만큼 이동하고 충전 카운트를 올린다.
            for r_sta in lst[:cnt:-1]:

                if sta >= r_sta:
                    sta = r_sta + K
                    cnt += 1
            #현재 위치가 다음 정거장을 못넘으면 작다면 0을 리턴한다
            print('sta', end='')
            print(sta)
            print('lst', end='')
            print(lst[cnt+1])
            if sta < lst[cnt+1]:
                return 0

            n += 1




testNum = int(input())

for test in range(1, testNum+1):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))


    print(f'#{test} {staNum(K,N,M,lst)}')