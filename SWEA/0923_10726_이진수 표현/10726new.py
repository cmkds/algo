import sys
sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum + 1):

    N, M = map(int, input().split())

    if M %2 :
        chk = 0
        a = str(format(M, 'b'))
        if len(a) >= N:
            for i in range(1, N + 1):
                if a[-i] == '0':
                    print(f'#{test} OFF')
                    break
            else:
                print(f'#{test} ON')
        else:
            print(f'#{test} OFF')
    else:
        print(f'#{test} OFF')