def preorder(n):
    if n<=N:
        a.append(n)
        preorder(2*n)
        preorder(2*n+1)

N = int(input())
z = list(map(int,input().split()))
d = int(input())
lst = [i for i in range(N+1)]
print(lst)
a=[]
preorder(d+1)
print(a)

for j in range(len(a)):
    for i in range(len(lst)):
        if lst[i] == a[j]:
            lst[i] = 0
            break
print(lst)

res = 0
for i in range(len(lst)):
    if lst[i] * 2 > N:
        res += 1
    elif lst[i]:
        if not (lst[lst[i]*2] or lst[lst[i]*2+1]):
            res += 1

print(res)