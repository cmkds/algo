import sys

sys.stdin = open('input.txt')

testNum = int(input())
for test in range(1, testNum+1):
    N = int(input())                        ##들어올 덱 카드 수 변수
    deck = list(map(str,input().split()))   ##인풋을 deck리스트로 한번에 받는다.

    aDeck = []                              #앞의 절반을 담을 aDeck
    bDeck = []                              #뒤어 절반을 담을 bDeck
    for i, dec in enumerate(deck):
        #전체 카드수가 홀수 일때
        if N % 2:
            if i < (N//2+1):
                aDeck.append(dec)
            else:
                bDeck.append(dec)
        #짝수 일때
        else:
             if i < (N//2):
                aDeck.append(dec)
             else:
                bDeck.append(dec)

    chkA = 0                     ###A덱이 종료됐는지 판단할 변수
    chkB = 0                     ###B덱이 종료됐는지 판단할 변수
    i = 0                        ###인덱스를 담을 변수
    printLst = []
    while chkA == 0 or chkB ==0:
        try:
            printLst.append(aDeck[i])
        except IndexError:
            chkA = 1
        try:
            printLst.append(bDeck[i])
        except IndexError:
            chkB = 1
        i += 1

    print(f'#{test}', end = ' ')
    print(*printLst)



