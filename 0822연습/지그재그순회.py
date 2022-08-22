n=4
m=3
lst =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

for i in range(n):
    for j in range(m):
        print(lst[i][j+(m-1-2*j)*(i%2)])
        ##홀수 행 일 때는 [j]
        ##짝수 행 일 때는 [m-1-j]
