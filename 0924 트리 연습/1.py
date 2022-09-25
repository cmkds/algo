import sys
sys.stdin = open('baek1991.txt')

def preorder(s):
    if s != 0:
        ans.append(T[s])
        preorder(ch1[s])
        preorder(ch2[s])
    return ans

def inorder(s):
    if s != 0:
        inorder(ch1[s])
        ans.append(T[s])
        inorder(ch2[s])
    return ans

def postorder(s):
    if s != 0:
        postorder(ch1[s])
        postorder(ch2[s])
        ans.append(T[s])
    return ans

n = int(input())

dict_a = dict()
for i in range(n):
    dict_a[f'{chr(65+i)}'] = i+1
print(dict_a)
T = [0] + [chr(i) for i in range(65, 65+n)]

ch1 = [0 for _ in range(n+1)]
ch2 = [0 for _ in range(n+1)]

for i in range(n):
    p, l, r = input().split()
    if l != '.':
        ch1[dict_a[p]] = dict_a[l]
    if r != '.':
        ch2[dict_a[p]] = dict_a[r]

ans = []
print(''.join(preorder(1)))

ans = []
print(''.join(inorder(1)))

ans = []
print(postorder(1))
print(''.join(postorder(1)))
print(ans)