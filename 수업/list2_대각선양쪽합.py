N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#대각선을 제왜 한 양쪽중 어디가 더 클까?
#1
s1=0
s2=0

for i in range(N):
    for j in range(N):
        if i>j:
            s1 += arr[i][j]
        elif i < j:
            s2 += arr[i][j]
print(s1,s2)

#2
s1=0
s2=0

for i in range(N):
    for j in range(i+1, N):
            s2 += arr[i][j]
            s1 += arr[j][i]
print(s1,s2)