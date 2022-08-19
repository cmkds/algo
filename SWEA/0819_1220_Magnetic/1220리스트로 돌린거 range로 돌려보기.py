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
            if lst[i][j] == 1:
                break
            elif lst[i][j] == 2:
                lst[i][j] = 0
    ##뒤쪽 처리하기
    for i in range(100):  ##이중배열 돌리기
        for j in range(99,-1,-1):  ##행마다 계산
            if lst[i][j] == 2:
                break
            elif lst[i][j] == 1:
                lst[i][j] = 0

    ##그리고 붙히고 교착상태 계산하기
    ####계산방법
    ###빈스택일때 1을 쌓는다. ### 앞의 2는 다 날렸으니 1부터 찾게된다.
    ####1을 먼저 찾아서 스택에 넣는다
    ####1이오면 무시한다
    ####0이오면 무시한다

    ####2가오면 쌓는다.
        #####
        #######가오면 쌓는다.  ###스택에는 1,2만 쌓인다.
        ###스택의 끝값이 1인지 2인지 if문 구분하고
        ######0이오면 카운트를 +1하고 스택을 지운다.

    cnt = 0
    stack = []  ##행마다 반복할 스택을 만든다.
    for a in lst:
        for i in range(100):
            ####비어있을때는 무조건 1이 들어온다.
            if not stack:
                if a[i] == 1:
                    stack.append(a[i])
            ##탑이 1일때
            elif stack[-1] == 1:
                if a[i]==2:
                    stack.append(a[i])
                    del stack
                    cnt += 1
                    stack =[]
            ###탑이 2일때
            # elif stack[-1] == 2:
            #    # if a[i] ==0:
            # 
            #     if a[i]==1:




    print(f'#{test} {cnt}')
