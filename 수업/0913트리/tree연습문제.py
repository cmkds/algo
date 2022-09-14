'''
정점 번호 V: 1~(E+1)
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''
def find_root(V):       #################################
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


def preorder(n):  #전위순회
    if n:
        print(n, end=' ')  #visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):  #중위순회
    if n:
        inorder(ch1[n])
        print(n, end=' ')  # visit(n)
        inorder(ch2[n])

def postorder(n):  #후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')  # visit(n)

V = int(input())     ##정점 개수, 마지막 정점 번호
arr = list(map(int,input().split()))
# root = 1  # root가 1번인걸 알고있다 치자.
E = V - 1
#부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

#자식을 인덱스로 부모 번호 저장
par = [0]*(V + 1)     ####################

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    if ch1[p] ==0: #아직 자식이 없으면
        ch1[p] =c  #자식1로 저장
    else:
        ch2[p] =c
    par[c] = p   #####################

root = find_root(V)
print(root)

# print(ch1)
# print(ch2)
preorder(root)
print()
inorder(root)
print()
postorder(root)