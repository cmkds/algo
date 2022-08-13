import sys

sys.stdin = open('input.txt')


def acnt(N, K, lst):
    ###리턴할 변수 카운트
    cnt = 0
    for i in range(N):
        tmpCnt = 0
        for j in range(N):
            #### 1일 때 tmpcnt +1
            if lst[i][j] == 1:
                tmpCnt += 1
            if lst[i][j]==0:
                ## 0이될따 tmpCnt가 K와 같았다면 cnt +1
                if tmpCnt == K:
                    cnt += 1
                tmpCnt = 0
            ###마지막에 도착했을 때 1이면 tmpCnt가 K인지 확인후 cnt +1
            if j == N-1 and tmpCnt == K and lst[i][-1] == 1:
                cnt +=1

    return cnt


testNum = int(input())

for test in range(1, testNum + 1):
    N, K = map(int, input().split())

    lst = [list(map(int, input().split())) for i in range(N)]

    a = acnt(N, K, lst)
    #리스트 행열 바꾼후 함수에 다시 넣기
    lst2 = list(zip(*lst))

    b = acnt(N, K, lst2)
    print(f'#{test} {a+b}')
