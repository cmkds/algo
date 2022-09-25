def preorder(N,tree):
    if N<=n:
        tree.append(N)
        preorder(2*N,tree)
        preorder(2*N+1,tree)

#####왼쪽 오른쪽 구분
###오른쪽이의 마지막이 반절을 넘어가면 똑같이 계산할 수 있다
##아닐때는 왼쪽오른쪽 구분해야한다.
##일단 꼭대기 까지 올리고 반대편 바닥까지 계산한다.

testNum = int(input())

for test in range(1,1+testNum):
    n, V = map(int,input().split())
    # binaryTree = list(i for i in range(n+1))

    # print(binaryTree)
    #왼쪽트리 오른쪽 트리 찾기
    res = 0
    if n ==1:
        res =0
    elif n ==2:
        res = 1
    else:
        leftTree = []
        rightTree = []
        preorder(2, leftTree)
        preorder(3, rightTree)
        # print(leftTree)
        # print(rightTree)   제대로 나옴 굳
        while V:
            V //= 2
            res += 1
        if V in leftTree:
            a = max(rightTree)
            while a:
                a //=2
                res += 1
        else:
            a = max(leftTree)
            while a:
                a //= 2
                res += 1
        res -= 2

    print(f'#{test} {res}')