import sys

sys.stdin = open('input.txt')

for _ in range(10):
    test = int(input())
    lst = [list(map(int, input().split())) for i in range(100)]

    # 움직일놈의 x,y 좌표 변수 설정
    x, y = 0, 99
    # 내가 보기 편하려고 X,Y로 설정했고
    # 리스트 안에서는 [Y,X] 임.
    ### moveIdx = 0

    for idx in range(100):
        if lst[99][idx] == 2:
            x = idx
    print(x)
    # 위로 한칸 보내고 양옆 같이 찾기 시작.
    y -= 1

    direction = 0  # 왼쪽이 우선순위 인지 오른쪽이 우선순위 인지 확인할 변수
    # x는 0일때 99일때 방향전환. 오른쪽은 1 왼쪽은 -1
    # 왼쪽은 없는데 오른쪽 일때 방향전환
    # 오른쪽 없는데 왼쪽은 있을때 방향 전환

    ### 첫 방향전환 나오기 전까지 위쪽으로 올리고 방향을 정해주는 코드
    #좌측벽일때 우측벽일때 아닐때 3가지
    if x==0:
        while lst[y][x + 1] == 0:
            # if lst[y - 1][x] == 1:
                y -= 1
    elif x== 99:
        while lst[y][x - 1] == 0:
            # if lst[y - 1][x] == 1:
                y -= 1
    else :
        while lst[y][x - 1] == 0 and lst[y][x + 1] == 0:
            # if lst[y - 1][x] == 1:
                y -= 1
    # 첫값이 좌측이면
    if x > 0 and lst[y][x - 1] == 1:
        direction = -1
        x -= 1

    # 첫값이 우측이면
    if x < 99 and lst[y][x + 1] == 1:
        direction = 1
        x += 1


    # 맨위에 도착할때까지 while 문 반복
    while y > 0:
        ##왼쪽 벽일때
        if x == 0:
            direction = 1

        ##오른쪽 벽일때
        if x == 99:
            direction = -1





        #########################################
        ## 왼쪽 조사 (왼쪽이 있으면 우선 순위가  왼 , 오른쪽 우선순위로 보내기, 위쪽 이됨)
        # 왼쪽이 있으면 한번은 무조건 보내고 그다음부터는 위쪽이 있으면 위쪽으로 보내야됨
        if direction == -1:
            if x > 0:
                if lst[y][x - 1] == 1:

                    direction = -1

                    if y == 0:
                        break
                    x -= 1
            if x == 0:
                direction = 1

            if x > 0:  # 왼쪽 벽에 붙었을 때는 왼쪽 조사를 하지 않는다.
                while lst[y][x - 1] == 1:  # 계속가다가 만약 위쪽이 1이라면 break하고 위쪽으로 간다.

                    if lst[y - 1][x] == 1:
                        break
                    if y == 0:
                        break
                    x -= 1  # x를 왼쪽으로 한칸 보낸다.

                    if x == 0:
                        direction = 1
                        break
            #@@@@@@@@@@@@@@@@@@@




        if direction == 1:
            ## 오른쪽조사 (오른쪽이 있으면 우선순위가 오른쪽, 왼쪽 (우선순위로 보내기, 위쪽이됨)
            if x < 99:  # 오른쪽 벽에 붙었을 때는 오른쪽 조사를 하지 않는다.
                if lst[y][x + 1] == 1:
                    direction = 1
                    if y == 0:
                        break
                    x += 1
            if x == 99:
                direction = -1

            if x < 99:
                while lst[y][x + 1] == 1:  # 오른쪽이 1일때 동안
                    if lst[y - 1][x] == 1: #만약 위쪽이 1이라면 break
                        break
                    if y == 0:
                        break
                    x += 1  # x를 오른쪽으로 한칸 보낸다.

                    if x==99:
                        direction= -1
                        break

        ## 위쪽조사. 왼쪽변에있을때는 왼쪽빼고 오른쪽벽에있을 때는 오른쪽빼고
        # 왼쪽 오른쪽 값이 둘다 없으면 위로 한칸
        # while lst[y]
        #     if lst[y - 1][x] == 1:
        #         y -= 1

        ### 처음에 위로가다가 왼쪽이 나오면 왼쪽으로가. 왼쪽으로 가다가 위쪽이 나오면 위쪽으로가
        ### 가다가 왼쪽이 나오면 왼쪽으로 가고  그런데 왼쪽이 0 인데 오른쪽이 1이면 오른쪽으로가
        #######왼쪽 오른쪽 둘다 없을때 위로 한칸 보냄


        ###############위로가다가 다이렉션 정방향인곳 나올때

        ### 다이렉션이 우측인데 좌측으로 바꿔야 하는 경우
        ## 우측은 0 좌측은 1일때



        y -= 1


        if direction == 1 and 0 < x < 99 :
            if lst[y][x + 1] == 0 and lst[y][x - 1] == 1:
                direction = -1
        ### 반대로 다이렉션이 좌측인데 우측으로 바꿔야 하는 경우
        ## 우측은 1 좌측은 0 일때
        if direction == -1 and 0 < x < 99 :
            if lst[y][x + 1] == 1 and lst[y][x - 1] == 0:
                direction = 1



    print(f'#{test} {x}')
