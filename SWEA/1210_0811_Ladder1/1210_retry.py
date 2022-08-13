import sys

sys.stdin = open('input.txt')

###처음 올라갈때  ##x가 0 , 99인 경우를 나누고


for _ in range(10):
    test = int(input())
    lst = [list(map(int, input().split())) for i in range(100)]

    # 움직일놈의 x,y 좌표 변수 설정
    x, y = 0, 99
    # 내가 보기 편하려고 X,Y로 설정했고
    # 리스트 안에서는 [Y,X] 임.

    for idx in range(100):
        if lst[99][idx] == 2:
            x = idx
    #도착위치를 찾고 역순으로 찾아 올린다.

    ############위로가다가 양옆에 1이 나오면 확인후 다이렉션 방향으로 이동.
    ############이때는 옆으로가다가 위에 1이나오면 위로이동
    ##########없으면 다이렉션 반대로 돌리고
    ##왼쪽확인    : lst[y][x - 1] == 1:
    ##오른쪽확인  : lst[y][x + 1] == 1:
    ##위쪽확인   : lst[y - 1][x] == 1
    direction =0




    ### 첫 방향전환 나오기 전까지 위쪽으로 올리고 방향을 정해주는 코드
    #좌측벽일때 우측벽일때 아닐때 3가지
    if x==0:
        while lst[y][x + 1] == 0:
                y -= 1
        direction = 1
        x += 1
    elif x== 99:
        while lst[y][x - 1] == 0:
                y -= 1
        direction = -1
        x -= -1
    else :
        while lst[y][x - 1] == 1 or lst[y][x + 1] == 1:
                y -= 1

    # 첫값이 좌측이면
    if x > 0 and lst[y][x - 1] == 1:
        direction = -1
        # x -= 1

    # 첫값이 우측이면
    if x < 99 and lst[y][x + 1] == 1:
        direction = 1
        # x += 1


    # 맨위에 도착할때까지 while 문 반복
    # while y > 0:
    #     ####################################################
    #     if direction == 0:
    #         while lst[y][x + 1] == 1 or lst[y][x - 1] == 1:
    #             y -= 1
    #         if lst[y][x + 1] == 1:
    #             direction = 1

    while y > 0:
        while x == 0 or x == 99:
            ###좌측 벽일때   우측만 확인해야함
            if x == 0:
                if lst[y][x + 1] == 0:
                    y -= 1
                else :
                    direction = 1
                    x += 1
            ###우측 벽일때   좌측만 확인해야함
            elif x == 99:
                if lst[y][x - 1] == 0:
                    y -= 1
                else :
                    direction = -1
                    x -= -1

                #while lst[y][x + 1] == 1 or lst[y][x - 1] == 1:
                ##왼쪽확인    : lst[y][x - 1] == 1:
                ##오른쪽확인  : lst[y][x + 1] == 1:
                ##위쪽확인   : lst[y - 1][x] == 1

        while 0 < x < 99:
            if lst[y][x + 1] == 1 or lst[y][x - 1] == 1:
                if direction == -1 and lst[y][x - 1] == 1:
                    x -= 1
                elif direction == 1 and lst[y][x + 1] == 1:
                    x += 1

                else:
                    y -= 1
                    if direction == -1 and lst[y][x + 1] == 1 and lst[y][x - 1] == 0:
                        direction = -1
                    elif  direction == 1 and lst[y][x - 1] == 1 and lst[y][x + 1] == 0:
                        direction = 1

            #올라갔는데 다이렉션과 다른방향에 길이있으면 다이렉션방향바꾸기





    print(f'#{test} {x}')
