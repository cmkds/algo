import sys
sys.stdin = open('14075.txt')

testNum = int(input())

for test in range(1,1+testNum):
    #노드수, 리프노드수, 출력할 노드 번호
    N, M, L = map(int,input().split())
    lst = [0] * (N+1)
    for i in range(M):
        a, b = map(int,input().split())
        lst[a] = b

    for i in range(N, 1, -1):
        lst[i//2] += lst[i]
    # print(lst)

    print(f'#{test} {lst[L]}')