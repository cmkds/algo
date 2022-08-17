import sys

sys.stdin = open('input.txt')

testNum = int(input())

# def pascal(lst,N):
#     for i in range(N-1,0,-1):
#         if lst[i][i] == 0:
#             lst[i][i]= lst[i-1][i]+lst[i-1][i-1]
#     return lst
def pascal(lst,N):
    for i in range(1,N):
        for j in range(1,i):
            if lst[i][j] == 0:
                lst[i][j]= lst[i-1][j]+lst[i-1][j-1]

# def fibo(n):
#      if n < 2:
#          return n
#      else:
#          return fibo(n-1) + fibo(n-2)


for test in range(1, testNum+1):
    N= int(input())

    lst = [[0] * i for i in range(1,N+1)] #0으로 삼각형 초기화 하기
    for i in range(N):
        lst[i][0] = lst[i][-1] = 1   #리스트 양쪽끝 1 할당

    pascal(lst,N)

    print(f'#{test}')
    for a in lst:
        print(' '.join(map(str, a)))
