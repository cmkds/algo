import sys
sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1,1+testNum):

    N, M, L = map(int,input().split())

    lst = [0]*(N+1)
    for i in range(M):
        idx, num = map(int,input().split())
        lst[idx]=num

    for i in range(N-M,0,-1):
        try :
            lst[i] = lst[i*2]+lst[i*2+1]
        except IndexError:
            lst[i] = lst[i*2]
    print(f'#{test} {lst[L]}')