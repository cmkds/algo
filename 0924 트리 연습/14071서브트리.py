import sys
sys.stdin = open('14071.txt')

def inorder(n):
    global cnt
    if n:
        inorder(ch1[n])
        cnt += 1
        inorder(ch2[n])

testNum = int(input())

for test in range(1,1+ testNum):
    E, root = map(int,input().split())
    V = E + 1
    lst = list(map(int,input().split()))

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    for i in range(0,E*2,2):
        if not ch1[lst[i]]:
            ch1[lst[i]] = lst[i+1]
        else:
            ch2[lst[i]] = lst[i+1]
    cnt = 0
    inorder(root)
    print(f'#{test} {cnt}')