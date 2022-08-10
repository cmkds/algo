'''
각행의 합을 구하고 그 중 최대값을 출력하시오
3
1 2 3
4 5 6
7 8 9
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s=0
for i in range(N):
    for j in range(N):
        if i==j:
            s += arr[i][j]

s=0
for i in range(N):
    s += arr[i][i]

print(s)

#######두 대각선의 합을 구할 때 배열의 크기가 홀수인 경우는 가운데값을 한번 빼주어야한다.