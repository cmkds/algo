import sys

sys.stdin = open('input.txt')

testNum = int(input())
####dp??? 비슷하게 구현. 따로 리스트는 안만듬.

def pascal(lst,N):
    for i in range(1,N):
        for j in range(1,i):
            if lst[i][i-j] !=0:   ##파스칼은 양쪽이 같은 모양이니 왼쪽에 값이있다면 오른쪽은 계산하지 않고 반대편 값을 바로 넣으면됨
                lst[i][j] = lst[i][i-j]

            elif lst[i][j] == 0:
                lst[i][j]= lst[i-1][j]+lst[i-1][j-1]




for test in range(1, testNum+1):
    N= int(input())

    lst = [[0] * i for i in range(1,N+1)] #0으로 삼각형 초기화 하기
    for i in range(N):
        lst[i][0] = lst[i][-1] = 1   #리스트 양쪽끝 1 할당

    pascal(lst,N)

    print(f'#{test}')
    for a in lst:
        print(' '.join(map(str, a)))
