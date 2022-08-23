import sys
from pprint import pprint
sys.stdin = open('input.txt')

def DFS(startHaeng,startYul):
    global dochak
    pprint(miro)
    if miro[startHaeng][startYul] ==3:
        dochak =1
        return
    elif dochak == 0:
        #위탐색
        if miro[startHaeng - 1][startYul] == 0 or miro[startHaeng - 1][startYul] == 3:
            miro[startHaeng][startYul] = 1
            DFS(startHaeng - 1, startYul)
            miro[startHaeng][startYul] = 0
        #아래 탐색
        if miro[startHaeng + 1][startYul] == 0 or miro[startHaeng + 1][startYul] == 3:
            miro[startHaeng][startYul] = 1
            DFS(startHaeng + 1, startYul)
            miro[startHaeng][startYul] = 0

        #왼쪽 탐색
        if miro[startHaeng][startYul - 1] == 0 or miro[startHaeng][startYul - 1] == 3:
            miro[startHaeng][startYul] = 1
            DFS(startHaeng, startYul - 1)
            miro[startHaeng][startYul] = 0

        #오른쪽 탐색
        if miro[startHaeng][startYul + 1] == 0 or miro[startHaeng][startYul + 1] == 3:
            miro[startHaeng][startYul] = 1
            DFS(startHaeng, startYul + 1)
            miro[startHaeng][startYul] = 0


testnum = int(input())
for test in range(1,testnum+1):

    N= int(input())
    #####미로 인풋을 처음부터 1로 감싸서 리스트에 받기
    miro = [[1]*(N+2)] + [[1]+list(map(int,input()))+[1] for i in range(N)]  + [([1]*(N+2))]

    ######시작 좌표 찾기
    for i in range(N+2):
        for a, num in enumerate(miro[i]):
            if num == 2:
                startHaeng = i
                startYul = a

    dochak = 0
    DFS(startHaeng,startYul)

    print(f'#{test} {dochak}')