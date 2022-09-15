import sys
sys.stdin = open('input.txt')

def pre(n):
    if n <= size:
        pre(2*n)
        idxLst.append(n)
        pre(2*n+1)

testNum = int(input())

for test in range(1,testNum+1):
    n = int(input())
    tree = [0]
    for i in range(1,n+1):
        tree.append(i)
    size = len(tree) - 1
    print(tree)
    idxLst=[0]
    pre(1)
    print(idxLst)

    print(f'#{test} {idxLst.index(1)} {tree[idxLst.index(n//2)]}')
    # print(idxLst.index(1))
    # print(tree[idxLst.index(n//2)])

