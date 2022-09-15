import sys
sys.stdin = open('input.txt')


def inorder(n):  #중위순회
    global res
    if n:
        inorder(nodeL[n])
        res += lst[n-1][1]   ### 출력할 문자열에 노드의 값 추가.
        inorder(nodeR[n])


for test in range(1,11):
    E = int(input())
    lst = [list(input().split()) for i in range(E)]

    root = 1                ###루트 정점의 번호는 항상 1
    V = E + 1

    # 부모를 인덱스로 자식 번호 저장 할 리스트 만들기.
    nodeL = [0] * (V + 1)
    nodeR = [0] * (V + 1)

    for i in range(E):
        try:
            p = int(lst[i][0])              ##부모 위치 설정
            j=2                             ##인덱스 잡는 변수 j
            while lst[i][j]:
                c = int(lst[i][j])

                if nodeL[p] == 0:  # 아직 자식이 없으면
                    nodeL[p] = c  # 왼쪽 자식에 저장
                else:              #있으면
                    nodeR[p] = c    #오른쪽 자식에 저장
                j += 1
        except IndexError:       ## 자식이 없을 시.
            continue
    # print(nodeL)
    # print(nodeR)
    res =''
    inorder(root)                   ##정점 부터 탐색

    print(f'#{test} {res}')