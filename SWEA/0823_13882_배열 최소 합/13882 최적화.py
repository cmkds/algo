import sys

sys.stdin = open('input.txt')

#순열 구하는 함수.
def f(i, r):
    global myMin
    if sum(soonyulHabLst[:i]) > myMin:
        return
    if i==r:
        if sum(soonyulHabLst) < myMin:
            myMin = sum(soonyulHabLst)
        return

    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            soonyulHabLst[i] = lst[i][n]
            f(i+1,r)

testNum = int(input())
for test in range(1,testNum+1):
    N = int(input())
    lst = [list(map(int,input().split())) for i in range(N)]


    bit = [0]*N  ### 순열을 받기 위한 리스트

    soonyulHabLst = [0]*N  ##순열을 담을 리스트
    myMin = 10 * N
    f(0, N)      ### 오른쪽 값에는 몇개가 들어가는지가 들어감. 여기서는 N개


    print(f'#{test} {myMin}')