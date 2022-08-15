import sys

sys.stdin = open('input.txt')

##진짜 문제 설명 왜이럼??????
testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())   #버스 노선수
    lst = [list(map(int, input().split())) for _ in range(N)]   # [1,3] [2,5]

    P = int(input())
    #dumiLst = [list(input()) for i in range(P)]  # 이건 더미 데이터로 날림 처리
    dumiLst = [list(input()) for i in range(P)]  #이건 더미 데이터로 날림 처리

    # print(dumiLst[-1][0])
    newLst = [0]*int(dumiLst[-1][0])

    for a in range(N):  #버스 노선 수만큼 돌려줌
        for b in range(lst[a][0]-1,lst[a][1]): 
            newLst[b] = newLst[b]+1    #버스가 지나가면 newLst b 에 +1해줌

    print(f"#{test} {' '.join(map(str,newLst))}")