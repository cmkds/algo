n = int(input())
lst = list(map(int,input().split()))

m =max(lst)
newLst=[0]*n
for i in range(n):
    newLst[i]= lst[i]/m*100

print(sum(newLst)/len(newLst))