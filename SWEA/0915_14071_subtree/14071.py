import sys
sys.stdin = open('input.txt')


def cnt(n):
    if n==0:
        return 0
    else:
        L = cnt(ch1[n])
        R = cnt(ch2[n])
        return L + R + 1

testNum = int(input())

for test in range(1,1+testNum):
    E, N = map(int,input().split())
    V = E + 1

    lst = list(map(int,input().split()))

    ch1 =[0]*(V+1)
    ch2 =[0]*(V+1)

    for i in range(E):
        p,c = lst[i*2],lst[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c


    print(f'#{test} {cnt(N)}')


