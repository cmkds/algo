import sys

sys.stdin = open('input.txt')

##진짜 문제 설명 왜이럼??????
testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())   #버스 노선수
    lst = [list(map(int, input().split())) for _ in range(N)]   # [1,3] [2,5]

    P = int(input())
    stationLst = []      ###스테이션 번호를 담을 리스트
    for i in range(P):
        stationLst.append(int(input()))

    newLst = [0]*5000

    for a in range(N):  #버스 노선 수만큼 돌려줌
        for b in range(lst[a][0]-1,lst[a][1]): 
            newLst[b] = newLst[b]+1    #버스가 지나가면 newLst b 에 +1해줌

    resLst = []
    #버스 노선 개수 리스트에서 스테이션 위치 찾아서 넣기 새로운 출력용 리스트에 넣기
    for station in stationLst:
        resLst.append(newLst[station-1])


    print(f"#{test} {' '.join(map(str,resLst))}")