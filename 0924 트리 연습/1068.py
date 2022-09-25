def preorder(n):
    if n<=101:
        a.append(n)
        preorder(2*n)
        preorder(2*n+1)

N = int(input())
z = list(map(int,input().split()))
d = int(input())

lst = [0,1]+[0] * (202)

for i in range(N):
    z[i] += 1

newLst = []
for idx, i in enumerate(z):
    newLst.append((i,idx))
newLst.sort()


for i in range(1, N):
    if not lst[lst.index(newLst[i][0])*2]:
        lst[lst.index(newLst[i][0])*2] = newLst[i][1]+1
    else:
        lst[lst.index(newLst[i][0])*2+1] = newLst[i][1]+1

a=[]
preorder(lst.index(d+1))


for j in range(len(a)):
    lst[a[j]] = 0


res = 0
for i in range(len(lst)):
    if lst[i] * 2 > N:
        res += 1
    elif lst[i]:
        if not (lst[lst[i]*2] or lst[lst[i]*2+1]):
            res += 1

print(res)