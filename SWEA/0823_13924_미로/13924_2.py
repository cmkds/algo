import sys

sys.stdin = open('input.txt')

def DFS(startHaeng,startYul):
    global dochak, chk
    if miro[startHaeng][startYul] == 3:
        dochak = 1
    else:
        #위탐색
        if miro[startHaeng - 1][startYul] == 0 and visited[startHaeng - 1][startYul] ==0 and miro[startHaeng - 1][startYul] == 3:
            visited[startHaeng - 1][startYul] = 1
            DFS(startHaeng - 1, startYul)
        #아래 탐색
        if miro[startHaeng + 1][startYul] == 0 and visited[startHaeng +1][startYul] ==0 and miro[startHaeng + 1][startYul] == 3:
            visited[startHaeng + 1][startYul] = 1
            DFS(startHaeng + 1, startYul)
        #왼쪽 탐색
        if miro[startHaeng][startYul - 1] == 0 and visited[startHaeng][startYul -1] ==0 and miro[startHaeng][startYul - 1] == 3:
            visited[startHaeng][startYul - 1] = 1
            DFS(startHaeng, startYul - 1)
        #오른쪽 탐색
        if miro[startHaeng][startYul + 1] == 0 and visited[startHaeng][startYul +1] ==0 and miro[startHaeng][startYul + 1] == 3:
            visited[startHaeng][startYul + 1] = 1
            DFS(startHaeng, startYul + 1)



testnum = int(input())
for test in range(1,testnum+1):

    N= int(input())
    #####미로 인풋을 처음부터 1로 감싸서 리스트에 받기
    miro = [[1]*(N+2)] + [[1]+list(map(int,input()))+[1] for i in range(N)]  + [([1]*(N+2))]
    print(miro)

    ######시작 좌표 찾기
    for i in range(N+2):
        for a, num in enumerate(miro[i]):
            if num == 2:
                startHaeng = i
                startYul = a
    ###미로의 시작 좌표는
    print(miro[startHaeng][startYul])

    ######@@@@ 지나간 경로를 체크 하기 위한 visited 이중배열을 0으로 초기화
    #####@@@@ 필요할지 말지는 아직 모르겠음.
    visited = [[0]*(N+2) for _ in range(N+2)]
    print(visited)
    ######

    ###미로 탐색순서 상하좌우로 가자
    dochak = 0
    chk = 0
    visited[startHaeng][startYul] = 1
    DFS(startHaeng,startYul)
    print(visited)
    print(dochak)