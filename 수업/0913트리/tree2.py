##완전 이진트리 탐색
def pre(n):
    if n <= size:

        pre(2*n)

        pre(2*n+1)
        print(tree[n], end=' ')



tree = [0, 'A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O'] ## 완전이진트리..
size = len(tree) -1                      ## 마지막 정점 번호
pre(1)
