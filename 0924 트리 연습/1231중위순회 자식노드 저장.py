import sys
sys.stdin = open('1231.txt')

#중위 순회
def inorder(n):

    if n:
        inorder(ch1[n])
        print(lst[n-1][1], end='')
        inorder(ch2[n])

for test in range(1,11):
    #정점의 수 8 간선 E 정점 V
    V = int(input())
    lst = [list(input().split()) for _ in range(V)]

    root = 1

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)

    for i in range(V):
        pIdx = int(lst[i][0])
        try:
            for j in range(2,4):
                c = int(lst[i][j])

                if not ch1[pIdx]:
                    ch1[pIdx] = c
                else:
                    ch2[pIdx] = c
        except IndexError:
            continue
    print(f'#{test} ', end='')
    inorder(root)
    print()
