import sys
sys.stdin = open('input.txt')

for test in range(1,11):
    N = int(input())
    lst = [0]+[list(input().split()) for _ in range(N)]    ##인데스 =정점번호 로 쓰려고 [0]을 앞에 넣음

    for i in range(N,0,-1):
        try:
            lst[i][1] = int(lst[i][1])              ##리스트의 1번위치를 인트로 변환.
                                                    ##2가지 기능
                                                    ## 1)인풋 받을 때 str로 받았으니 숫자를 int로 변환, 밑에서 자식인덱스 찾을 때 쓰임
                                                    ## 2)int로 바꿀 때 에러가 나면 부호라는 것이니까
                                                    ##   밑에 except로 부호일 때 코드를 실행
        except ValueError:
            if lst[i][1] == '+':
                lst[i][1] = lst[int(lst[i][2])][1] + lst[int(lst[i][3])][1]    #좌우 자식노드 값을 찾아 해당 부호에 따른 계산 실행
            elif lst[i][1] == '-':
                lst[i][1] = lst[int(lst[i][2])][1] - lst[int(lst[i][3])][1]
            elif lst[i][1] == '*':
                lst[i][1] = lst[int(lst[i][2])][1] * lst[int(lst[i][3])][1]
            else:
                lst[i][1] = lst[int(lst[i][2])][1] / lst[int(lst[i][3])][1]

    print(f'#{test} {int(lst[1][1])}')      ##최종값 (루트노드) 출력