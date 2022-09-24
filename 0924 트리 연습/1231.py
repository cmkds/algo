import sys
sys.stdin = open('1231.txt')

def inorder(n):  # 중위순회
    global k
    if n:
        inorder(ch1[n])
        # print(n)  # visit(n)
        # newlst.append(n)
        k += lst[n - 1][1]
        inorder(ch2[n])


for test in range(1, 11):
    E = int(input())
    lst = [list(input().split()) for i in range(E)]
    # print(lst)

    root = 1
    V = E + 1
    # 부모를 인덱스로 자식 번호 저장
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    for i in range(E):
        try:
            p = int(lst[i][0])
            j = 2

            while lst[i][j]:
                c = int(lst[i][j])

                if ch1[p] == 0:  # 아직 자식이 없으면
                    ch1[p] = c  # 자식1로 저장
                else:
                    ch2[p] = c
                j += 1
        except:
            continue
    print(ch1)
    print(ch2)
    k = ''
    inorder(root)

    print(f'#{test} {k}')