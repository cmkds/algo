import sys

sys.stdin = open('input.txt')


def staNum(K,N,lst):

    cnt = 0             #충전횟수를 카운트 할 변수

    nowLoc = 0          #현재 위치를 저장할 변수


    while nowLoc + K < N :                      # nowLoc 현재위치 + K 이동가능거리가  N 종점을 넘으면 while 종료


        for k in range(K, 0, -1):              #최대 이동거리 부터 역순으로 이동거리안에 충전소가 여러개일 경우
                                               #가장 먼 충전소로 바로 이동하기 위함.

            if nowLoc+k in lst:                #이동 가능 거리에서 충전소가 있으면

                nowLoc += k                    #현재위치를 이동가능거리만큼 옮기고

                cnt += 1                       #충전 카운트 +1

                break                          #충전소를 찾으면 더이상 for문이 돌지 않도록 break

        else:                                  #위 for문이 break 없이 종료 됐을 때는 이동가능 거리에 충전소가 없었다는 것이므로
            return 0                           # 종점까지 가지못하므로 0을 return

    return cnt                                 #정상적으로 충전받아 종점에 도착했으면 충전 카운트를 리턴


testNum = int(input())

for test in range(1, testNum+1):
    K, N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))


    print(f'#{test} {staNum(K,N,lst)}')