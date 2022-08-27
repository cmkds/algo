import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test = int(input())
    sadari = [list(map(int,input().split())) for _ in range(100)]

#리스트를 만들고 첫번째줄이 1이면 출발 출발시키고 cnt를 저장하기

    dx = [-1, 1, 0]                     #이게 델타탐색이구만
    dy = [0,0,1]

    cntLst =[]                          #카운트를 담을 리스트
    idxLst =[]                          #카운트 리스트와 같은위치에 인덱스를 저장할 리스트

    for i in range(100):
        cnt = 0
        visited = [[0] * 100 for _ in range(100)]   ##이걸 안에 넣어서 계속 초기화 했어야지. 밖에 뒀다가 무한루프 발생.

        if sadari[0][i] == 1:                       #첫줄이 1일때 사다리 타기 시작

            x=i
            y=0
            visited[y][x] =1

            nY = 0                                  #while문에 nY가 들어가서 ny만 밖에서 초기화
            while nY != 99:
                for k in range(3):                  #델타탐색

                    nX= x+dx[k]
                    if nX == -1 or nX == 100:       #밖으로 삐져나갈때 이렇게 처리하니까 간단
                        continue
                    nY= y+dy[k]

                    if sadari[y][nX] ==1 and visited[y][nX] == 0:
                        x = nX
                        visited[y][nX] = 1
                        cnt +=1
                        break

                    elif sadari[nY][x] == 1 and visited[nY][x] ==0:
                        y = nY
                        visited[nY][x] = 1
                        cnt +=1
                        break

            idxLst.append(i)    
            cntLst.append(cnt)  

    #print(idxLst)   [0, 3, 14, 18, 23, 27, 31, 35, 46, 49, 58, 65, 67, 78, 89, 99]
    #print(cntLst)   [205, 160, 178, 196, 237, 192, 201, 238, 284, 273, 237, 287, 278, 272, 311, 269]

    minCnt = min(cntLst)                            #최소값 찾고
    idx = cntLst.index(minCnt)                      #인덱스 찾고
    res = idxLst[idx]                               #그 인덱스로 미로에서의 인덱스 찾기
    print(f'#{test} {res}')


