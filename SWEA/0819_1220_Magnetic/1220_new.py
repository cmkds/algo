for test in range(1, 11):

    N = int(input())
    # 배열 받기.
    lst = [list(map(int, input().split())) for i in range(N)]

    #### 옆으로 회전시키기
    for i in range(100):
        for j in range(100):
            if i > j:
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
        for j in range(99, -1, -1):  ##행마다 계산
            if lst[i][j] == 2:
                break
            elif lst[i][j] == 1:
                lst[i][j] = 0

    ##그리고 붙히고 교착상태 계산하기
    ##1을 넣고 2가 쌓이면 cnt +1

    cnt = 0
    stack = []  ##행마다 반복할 스택을 만든다.
    for a in lst:
        for i in range(100):
            ####비어있을때는 무조건 1이 들어온다.
            if not stack:
                if a[i] == 1:
                    stack.append(a[i])
            ##탑이 1일때 2가들어오면 cnt +1
            elif stack[-1] == 1:
                if a[i] == 2:
                    stack.append(a[i])
                    del stack
                    cnt += 1
                    stack = []

    print(f'#{test} {cnt}')