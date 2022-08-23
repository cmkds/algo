import sys

sys.stdin = open('input.txt')

#순열 구하는 함수.
def f(i, r):
    global soonyulLst

    if i==r:
        # print(bit[:r])
        soonyulLst.append(bit[:r])
        return
    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            f(i+1,r)

testNum = int(input())
for test in range(1,testNum+1):
    N = int(input())
    lst = [list(map(int,input().split())) for i in range(N)]


    bit = [0]*N  ### 순열을 받기 위한 리스트
    soonyulLst = []  ##순열을 담을 리스트
    f(0, N)      ### 오른쪽 값에는 몇개가 들어가는지가 들어감. 여기서는 N개


    myMin = 5000

    for a in range(len(soonyulLst)):
        tmpMin = 0
        for i in range(N):
            tmpMin += lst[i][soonyulLst[a][i]]
        if tmpMin < myMin:
            myMin = tmpMin
    print(f'#{test} {myMin}')