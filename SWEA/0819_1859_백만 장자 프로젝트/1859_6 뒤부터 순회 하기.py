import sys

sys.stdin = open('input2.txt')

testNum = int(input())


for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    tmp = 0
    for i in range(N-1,-1,-1):
        if tmp > lst[i]:
            cnt += tmp - lst[i]
        else :
            tmp = lst[i]


    print(f'#{test} {cnt}')