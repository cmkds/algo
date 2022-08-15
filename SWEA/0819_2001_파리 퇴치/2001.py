import sys

sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1, testNum+1):
    N , M = map(int, input().split())  # N*N 배열, M*M 도장

    lst = [list(map(int,input().split())) for i in range(N)]
    maxNum = 0
    ##for문 2개돌리면서 도장 크기를 tmpNum에 저장하고 maxNum보다 크다면 maxNum에 저장
    for i in range(N-M+1):  #아래로 N-M+1 만큼    이동할수 있음
        for j in range(N-M+1):  #우측으로 N-M+1 만큼  이동할수 있음
            tmpNum = 0
            for a in range(i,M+i):  #우측  도장크기만큼
                for b in range(j, M+j): #아래측 도장크기만큼
                    tmpNum += lst[a][b]
            if tmpNum > maxNum:
                maxNum = tmpNum
    print(f'#{test} {maxNum}')