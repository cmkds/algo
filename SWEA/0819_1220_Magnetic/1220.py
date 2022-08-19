import sys

sys.stdin = open('input.txt')


for test in range(1,11):
    ###인풋 받기.

    #배열 크기 받기
    N = int(input())
    #배열 받기.
    lst = [list(map(int, input().split())) for i in range(N)]

    #### 옆으로 회전시키기
    for i in range(100):
        for j in range(100):
            if i>j:
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]

    ####앞쪽먼저 처리하기
    for i in range(100):  ##이중배열 돌리기
        for j in range(100):  ##행마다 계산
            if lst[i][j] == 2:
                break
            elif lst[i][j] == 1:
                lst[i][j] = 0
    ##뒤쪽 처리하기
    for i in range(100):  ##이중배열 돌리기
        for j in range(99,-1,-1):  ##행마다 계산
            if lst[i][j] == 1:
                break
            elif lst[i][j] == 2:
                lst[i][j] = 0

    ##그리고 붙히고 교착상태 계산하기
    ###빨간거 1만 세고 그 사이에 0이 있을때만 카운트 해주면 된다.
    print(lst)
    ####계산방법
    ######2를 먼저 찾아서 스택에 넣는다
    ####2가오면 무시한다
    ####0이오면 무시한다

    ####1이 오면 쌓는다.
        #####1이오면 무시한다
        #######2가오면 쌓는다.  ###스택에는 1,2만 쌓인다.
        ###스택의 끝값이 1인지 2인지 if문 구분하고
        ######0이오면 카운트를 +1하고 스택을 지운다.

    cnt = 0
    for _ in lst:
        stack = [] ##행마다 반복할 스택을 만든다.
        print(stack)
        for now in _:
            ####비어있을때는 무조건 2가 들어온다.
            if not stack == True:
                if now ==2:
                    stack.append(now)
            ##탑이 2일때
            elif stack[-1] ==2:
                if now==1:
                    stack.append(now)
            ###탑이 1일때
            elif stack[-1] == 1:
                if now==2:
                    stack.append(now)
                elif now ==0:
                    del stack
                    cnt +=1
    print(cnt)
