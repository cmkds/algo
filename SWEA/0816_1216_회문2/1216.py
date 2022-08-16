import sys

sys.stdin = open('input2.txt')

for _ in range(1, 11):
    test = int(input())
    lst = [list(input()) for i in range(100)]

    bar = 100 #회문찾는 길이

    while bar >1: #길이가 1이되면 중지.
        chk = 0 #가장긴 회문을 찾으면 break하기 위한 변수
        #가로로 찾고
        for i in range(100):  # 전체 배열 돌리고
            for b in range(100-bar+1): #전체배열 - 막대길이 + 1 만큼 가면서 막대길이의 회문확인
                if lst[i][b:b+bar] == lst[i][b:b+bar][::-1]:
                    chk = 1
                    break        #찾으면 break
        if chk == 1:
            break
            
        lst = list(zip(*lst))       #회전하고 세로 찾고

        for i in range(100):
            for b in range(100-bar+1):
                if lst[i][b:b+bar] == lst[i][b:b+bar][::-1]:
                    chk =1
                    break
        if chk == 1:
            break

        bar -= 1

    print(f'#{test} {bar}')