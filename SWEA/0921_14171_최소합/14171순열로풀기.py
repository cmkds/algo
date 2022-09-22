import sys
sys.stdin = open('input.txt')


testNum = int(input())

def soonyul(N, lst):
    for i in range(N):
        for j in range(N):
            lst.append(i,j)


for test in range(1,1+testNum):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]

    #순열 만들기

