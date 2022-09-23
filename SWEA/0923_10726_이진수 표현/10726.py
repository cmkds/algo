import sys
sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1,testNum+1):

    N, M = map(int,input().split())

    # if M % 2:
    chk = 0
    print(M)

    a = str(format(M,'b'))
    print(a)
    # print('##########')
    if len(a) >= N:
        for i in range(1,N+1):
            if a[-i] == '0':
                chk = 0
                break
        else:
            chk = 1
    else:
        print(f'#{test} OFF')
        # try :
        #     if a[-i] == '1':
        #         # print(a[-i])
        #         chk = 1
        #         continue
        #     else:
        #         chk = 0
        #         break
        # except IndexError:
        #     chk = 0
        #     # print(f'#{test} OFF')
        #     break

    if chk == 1:
        print(f'#{test} ON')
    else:
        print(f'#{test} OFF')

    # else:
    #     print(f'#{test} OFF')
