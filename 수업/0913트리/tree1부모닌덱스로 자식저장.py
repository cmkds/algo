'''
정점 번호 V: 1~(E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5

'''

def preorder(n):  #전위순회
    if n:
        print(n)  #visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):  #중위순회
    if n:
        inorder(ch1[n])
        print(n)  # visit(n)
        inorder(ch2[n])

def postorder(n):  #후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)  # visit(n)

E = int(input())
arr = list(map(int,input().split()))
root = 1  # root가 1번인걸 알고있다 치자.
V = E + 1
#부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    if ch1[p] ==0: #아직 자식이 없으면
        ch1[p] =c  #자식1로 저장
    else:
        ch2[p] =c

# print(ch1)
# print(ch2)
preorder(root)