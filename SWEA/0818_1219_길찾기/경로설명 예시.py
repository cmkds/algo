import sys


sys.stdin = open('input.txt')
###
def DFS(v) :
    global cnt, path   ###글로벌 변수로 정해줘야 함수밖에서도 적용이 도니다
    if v==n:          ######v가  원하는 도착점에 도달했을때 작동하는 ㅗㅋ드
        cnt +=1       #####경로의 수를 카운트 한다.
        for x in path:   ######### 이때 지금까지 왔떤경로가 x lst에 있으므로 순서대로 출력한다.
            print(x, end=' ')
        print()
    else:             #########위의 경우가 아닐시 작동하는 코드
        for i in range(1,n+1):      ########## 간선들이 들어있는 리스트를 돌리기 위해 그 (n)갯수만큼 돌려준다.
            if g[v][i] == 1 and ch[i] ==0:    #####ch[i]는 내가 방문했던 것을 나타내는 리스트로
                                                ###방문하지 않았던 0 인경우에만 코드가 작동하도록 해준다.
                ch[i]=1                     ####이코드가 작동했다면 이제 방문하는 것이므로 ch[i]를 1로만들어준다.
                path.append(i)              #### 그리고 경로를 담은 리스트 path에 해당 노드 번호를 넣어준다.
                DFS(i)                      ###그리고 현재 노드에서 다시 경로찾기 함수를 돌려준다.
                                            ###여기서 함수들이 스택형태로 쌓인다.
                path.pop()                  ####경로를 다찾고빠져나왔을때 해당 경로를 path리스트에서 지워주고
                                            ###다른 방향으로 다시 탐색한다.

                ch[i]=0                     ## 방문확인 리스트에서도 값을 0으로 바꿔줘야하는데
                                            # why? 다른 경로에선 다시 지나갈수있어야 하기때문에
                                            ##또 위에 for문에서 i순서대로 돌고있기 때문에
                                            ##무한루프에 걸리지 않는다.

###

testNum = int(input())
for test in range(1, testNum + 1):
    n, m = map(int, input().split())  ###n은 노드의수 m 은 간선의 수
    ###

    g = [[0]*(n+1) for _ in range(n+1)]     ###경로를 저장할 리스트
    ch = [0] * (n+1)                        ###방문햇는지 안했는지를 나타낼 리스트 미방문시 0 방문시 1
    for i in range(m):
        a,b = map(int, input().split())     #경로를 받는코드
        g[a][b]= 1                          ###경로(간선)을 받아 경로리스트에 해당 위치를 1로 만들어준다.
    cnt =0                  ###경로의 수를 담을 변수
    ch[1] = 1                               ### start값을 추가시킨 코드
    path = list()                           ###지나가면서 노드경로를 담을 리스트를 만든것
    path.append(1)                          ###start값을 추가시킨것
    DFS(1)                                  ###start 값으로 DFS를 돌린다.
    print(cnt)                              ###cnt를 출력해주면 끝.