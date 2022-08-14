import sys

sys.stdin = open('input.txt')


def staNum(K,N,lst):
                                                    #충전할 카운트 변수
    cnt = 0
                                                    #현재 위치 변수
    nowLoc = 0

                                                        # nowLoc 현재위치 + K 이동가능거리가  N 종점을 넘으면 while 종료
    while nowLoc + K < N :
                                                            #k 한번이동 횟수 역순으로 for문 최대한 멀리 가야하니깐
        for k in range(K, 0, -1):                               #3 +5   lst [ 3 , 7  ,8 , 10]
                                                #이동 가능 거리에서 충전소가 있으면
            if nowLoc+k in lst:
                                                    #현재위치를 이동가능거리만큼 옮기고
                nowLoc += k
                                                        #충전 카운트 +1
                cnt += 1
                                                    #혹시 이동가능거리에 충전소가 여러개 있을수도 있으므로 break로 for문 종료
                break
                                                #위 for문이 break 없이 종료 됐을 때는 이동가능 거리에 충전소가 없었다는 것이므로
                                                # 종점까지 가지못하므로 0을 return
        else:
            return 0
                                                #정상적으로 충전받아 종점에 도착했으면 충전 카운트를 리턴
    return cnt


testNum = int(input())

for test in range(1, testNum+1):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))


    print(f'#{test} {staNum(K,N,lst)}')