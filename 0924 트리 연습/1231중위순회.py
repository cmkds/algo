import sys
sys.stdin = open('1231.txt')

#중위 순회
def inorder(n):
    if n<= size:
        inorder(n*2)
        print(lst[n], end='')
        inorder(n*2+1)

for test in range(1,11):
    #정점의 수 8 간선 E 정점 V
    V = int(input())
    lst = [0] * (V+1)  ## 트리 정보를 담을 리스트, 정점의 수 보다 한개 크게 만든다.

    for i in range(V):
        tmpLst = list(input().split())
        lst[int(tmpLst[0])] = tmpLst[1] ##인풋값의 첫번째 칸이 인덱스. 그 걸로 두번째칸
                                        ##문자의 값을 넣어준다.
    root = 1
    size = len(lst)-1
    print(f'#{test} ', end='')
    inorder(root)
    print()