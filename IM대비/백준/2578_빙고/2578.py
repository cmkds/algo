import sys
sys.stdin = open('input.txt')

##키는 숫자 값은 인덱스

def bingGoTamsaek(num):
    a, b = dic.get(num)
    chulSoo[a][b] =0            #철수 빙고의 해당 자리를 0으로 바꿔 버림
    cnt =0
    #가로탐색
    for i in range(5):
        if chulSoo[a][i] !=0:
            break
    else:
        cnt +=1
    #세로 탐색
    for i in range(5):
        if chulSoo[i][b] !=0:
            break
    else:
        cnt +=1
    #좌표가 같을때 대각선 탐색
    if a==b:
        for i in range(5):
            if chulSoo[i][i] !=0:
                break
        else:
            cnt +=1
    #좌표가 역대각선일때 역대각선 탐색
    if a+b == 4:
        for i in range(5):
            if chulSoo[i][4-i] !=0:
                break
        else:
            cnt +=1
    return cnt

########################

chulSoo = [list(map(int,input().split())) for _ in range(5)]        #철수 빙고판
bingGo = []
for _ in range(5):
    bingGo.extend(list(map(int,input().split())))         #사회자 빙고
                                                          ##extend로 넣으면 1차원 append로 넣으면 2차원


dic=dict()                                      #딕셔너리 만들기
for i in range(5):
    for j in range(5):
        dic[chulSoo[i][j]]=(i,j)


cnt = 0
bingGoCnt =0
for i in range(25):
    bingGoCnt += bingGoTamsaek(bingGo[i])
    cnt +=1
    if bingGoCnt >=3:       ###!!!  =3 으로 해서 틀렸음 >=3 으로 하기
        break

print(cnt)