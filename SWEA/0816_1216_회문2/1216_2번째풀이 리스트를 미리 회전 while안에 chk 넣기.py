import sys

sys.stdin = open('input.txt')

#리스트를 미리 회전해주고
#chk를 break로 안하고 while문으로 확인
for _ in range(1, 11):
    test = int(input())
    lst = [list(input()) for i in range(100)]
    newLst = list(zip(*lst))

    bar = 100
    chk = 0
    while bar >1 and chk == 0:

        for i in range(100):
            for b in range(100-bar+1):
                if lst[i][b:b+bar] == lst[i][b:b+bar][::-1]:
                    chk = 1
   
                if newLst[i][b:b + bar] == newLst[i][b:b + bar][::-1]:
                    chk = 1
        bar -= 1

    print(f'#{test} {bar+1}')  ##이경우는 while문에 break를 검증해서  마지막에 bar가 -1되고 나와서 +1 해줬음