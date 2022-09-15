import sys
sys.stdin = open('input.txt')

def inorder(n):             ##중위 순회 돌면서
    global k

    if n <= size:
        inorder(2*n)
        k += 1              ##1을 증가 시키면서
        tree[n] = k         ##그 값을 순회하는 위치에 입력
        inorder(2*n+1)

testNum = int(input())

for test in range(1,testNum+1):
    n = int(input())
    tree = [0]*(n+1)
    size = len(tree) - 1

    k =0
    inorder(1)

    print(f'#{test} {tree[1]} {tree[n//2]}')


