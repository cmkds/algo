import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    test = int(input())
    lst = [list(input()) for i in range(100)]
    newLst = list(zip(*lst))
    ##행열 바꾼 배열도 만들어 주고 같이 돌려서 확인한다.
    ### chk 1될때마다 브레이크 해준다.
    bar = 100

    while bar > 1:
        chk = 0

        for i in range(100):
            for b in range(100 - bar + 1):
                if lst[i][b:b + bar] == lst[i][b:b + bar][::-1]:
                    chk = 1
                    break
                if newLst[i][b:b + bar] == newLst[i][b:b + bar][::-1]:
                    chk = 1
                    break
            if chk == 1:
                break
        if chk == 1:
            break

        bar -= 1

    print(f'#{test} {bar}')