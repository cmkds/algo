import sys


sys.stdin = open('input.txt')
###
def DFS(A) :
    global dochak, path   ###글로벌 변수로 정해줘야 함수밖에서도 적용이 도니다
    if A==B:              ######A가  원하는 도착점 B에 도달했을때 작동하는 코드
        dochak = 1       #####경로의 수를 카운트 한다.
        # for x in path:   ######### 이때 지금까지 왔떤경로가 x lst에 있으므로 순서대로 출력한다.
        #     print(x, end=' ')
        # print()
    else:             #########위의 경우가 아닐시 작동하는 코드
        for i in range(1,n):      ########## 간선들이 들어있는 리스트를 돌리기 위해 그 (n)갯수만큼 돌려준다.
            if gansunLst[A][i] == 1 and visited[i] ==0:    ####visited[i]는 내가 방문했던 것을 나타내는 리스트로
                                                ###방문하지 않았던 0 인경우에만 코드가 작동하도록 해준다.
                visited[i]=1                     ####이코드가 작동했다면 이제 방문하는 것이므로 visited[i]를 1로만들어준다.
                path.append(i)              #### 그리고 경로를 담은 리스트 path에 해당 노드 번호를 넣어준다.
                DFS(i)                      ###그리고 현재 노드에서 다시 경로찾기 함수를 돌려준다.
                                            ###여기서 함수들이 스택형태로 쌓인다.
                path.pop()                  ####경로를 다찾고빠져나왔을때 해당 경로를 path리스트에서 지워주고
                                            ###다른 방향으로 다시 탐색한다.

                visited[i] = 0                     ## 방문확인 리스트에서도 값을 0으로 바꿔줘야하는데
                                            # why? 다른 경로에선 다시 지나갈수있어야 하기때문에
                                            ##또 위에 for문에서 i순서대로 돌고있기 때문에
                                            ##무한루프에 걸리지 않는다.

###
###출발점은 0, 도착점은 99
### 한 노드에서 간선의 개수 최대 2개

###테스트 번호,  간선의 수
#간선은 0 1  /   2 0  이렇게 주어진다
#만약 간선의 수가 16개라면 숫자 32개가 주어지는것
#이걸 스플릿해서 담아야 한다.
###일단 스플릿해서 한문장에 담고
## for문돌려서 앞에꺼는 시작 뒤에꺼는 끝에 담으면 될듯???

#시작점 A=0 도착점 B = 99 로 고정
### 노드의 수는 주어지지 않으므로 0~99로 초기화 해야한다.

###################이문제는 인풋 개수가 안주어지기 때문에 while문으로 돌려줘야한다.
    #######while을 돌리다가 input()이 없어서 에러가 뜬다면 그때 break해서 나오도록 try except넣어주면 될듯
###while True:
###@@@@@@@일단 while문은 마지막에하고 여기서 테스트 케이스는 10개이므로 10번 돌린다
for _ in range(10):
    #
    ####
    test, m = map(int, input().split())  ### m 은 간선의 수
    ###                                 ###이문제는 노드가 0부터 시작하므로
                                        ###노드가 1부터 시작하는 다른문제에서썼던
                                        ##+1 들어가는 과정이 없다.
    n = 100                             ##n은 노드의수 이문제에선 100개로 주어졌다.
    gansunLst = [[0]*(n) for _ in range(n)]     ###간선을 1로 나머지는 0으로 저장할 리스트
    visited = [0] * (n)               ###방문햇는지 안했는지를 나타낼 리스트 미방문시 0 방문시 1


    ##################여기서
    ###스플릿하고 하나씩 리스트에 넣고
    ###그 리스트를 돌려주면서 경로 리스트에 넣어줘야한다..
    lst = list(map(int,input().split()))
    #print(lst)

    for i in range(0, m*2, 2):     ####0에서 끝까지 2칸씩 점프시킨다.
        start = lst[i]
        end = lst[i+1]
        gansunLst[start][end] = 1   ###i는 시작노드 i+1 도착노드

    A = 0               #시작 노드
    B = 99              #도착 노드

    visited[A] = 1                          ### start값을 추가시킨 코드
    dochak = A                              ### 99에 도착했을시 1로 바뀔 dochak 변수
    
    path = list()                           ###지나가면서 노드경로를 담을 리스트를 만든것
    path.append(A)                          ###start값을 추가시킨것
    DFS(A)                                  ###start 값으로 DFS를 돌린다.
    print(f'#{test} {dochak}')                           ###dochak를 출력해주면 끝.