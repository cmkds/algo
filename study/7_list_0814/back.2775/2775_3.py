import sys

sys.stdin = open('input.txt')

def a(k,n):
    if k == 0 :
        return n
    elif n == 1:
        return 1

    return a(k-1,n)+a(k,n-1)

test = int(input())
for _ in range(test):
    k = int(input())
    n = int(input())
    # a = [[k], [n]]
    # tmp = 0
    # if k == 0:
    #     tmp += n
    # elif n == 1:
    #     tmp += 1
    # for _ in range(k)
    #
    # print(a(k,n))

    lst = [[0] * n for _ in range(k+1)]



    for i in range(k): #0~2
        for j in range(1,n+1): # 1~4
            if i == 0:
                lst[i][j-1] = j
            if j == 1 :
                lst[i][j] = 1
            else :
                lst[i][j-1] = lst[i-1][j-1]+lst[i][j-2]
    print(lst)
    print(lst[k][n-1])