import sys
sys.stdin = open('14073.txt')

def inorder(n):
    global k
    if n <= N:
        inorder(2*n)
        k += 1
        lst[n] = k
        inorder(2*n+1)

testNum = int(input())

for test in range(1, 1+testNum):

    N = int(input())
    lst = [0] * (N+1)
    k = 0
    inorder(1)
    print(f'#{test} {lst[1]} {lst[N//2]}')