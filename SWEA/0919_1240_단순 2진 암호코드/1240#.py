import sys
from pprint import pprint
sys.stdin = open('input.txt')

testNum = int(input())

dic = {
    '0001101':0 ,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}


for test in range(1,testNum+1):
    N , M = map(int, input().split())
    lst = [list(map(int,input())) for _ in range(N)]

    x =0
    y =0
    for i in range(N):
        if x:
            break
        for j in range(M-1,-1,-1):
            if lst[i][j] == 1:
                x = i
                y = j
                break

    stLst = []
    for i in range(y,y-56,-7):
        s = ''
        for j in range(7):
            s = str(lst[x][i-j]) + s
        stLst.append(s)
    stLst.reverse()

    chkLst = []
    for a in stLst:
        chkLst.append(dic.get(a))
    cnt = 0
    for i in range(0,8,2):
        cnt += chkLst[i]*3
        cnt += chkLst[i+1]

    if cnt % 10:
        print(f'#{test} 0')
    else:
        print(f'#{test} {sum(chkLst)}')
