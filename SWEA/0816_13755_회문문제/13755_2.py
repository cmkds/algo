import sys

sys.stdin = open('input.txt')

#다른 사람들 코드 보니깐 첫 for문을 range로 돌리네
#나만 lst로 돌렸네  근데 이거 바꿔서 맞으면 왜? 근데 또 채점 안될거 같은데
#첫 for문 lst에서 range(N)으로 바꿔서 돌림
testNum = int(input())

for test in range(1, testNum+1):
    N , M = map(int, input().split())

    lst = [list(input()) for i in range(N)]


    for i in range(N):
        for r in range(N-M+1):

            if lst[i][r:r+M] == lst[i][r:r+M][::-1]:
                res = ''.join(lst[i][r:r+M])



    lst = list(zip(*lst))

    for i in range(N):
        for r in range(N-M+1):

            if lst[i][r:r+M] == lst[i][r:r+M][::-1]:
                res = ''.join(lst[i][r:r+M])

    print(f'#{test} {res}')