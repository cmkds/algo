import sys
sys.stdin = open('input.txt')

def goosib(lst,n):
    newLst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newLst[j][n - 1 - i] = lst[i][j]
    return newLst

def baekpalsib(lst,n):
    newLst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newLst[n-1-i][n-1 -j] = lst[i][j]
    return newLst


def ebaekcil(lst,n):
    newLst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newLst[n - 1 - j][i] = lst[i][j]
    return newLst

t = int(input())
for test in range(1, t+1):
    n = int(input())


    lst = [list(map(int, input().split())) for i in range(n)]


    print(f'#{test}')
    for i in range(n):
        print(f"{''.join(map(str,goosib(lst,n)[i]))} {''.join(map(str,baekpalsib(lst,n)[i]))} {''.join(map(str,ebaekcil(lst,n)[i]))}")

