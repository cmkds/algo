a = int(input())
b = int(input())
c = int(input())

g = str(a*b*c)
chk =['0','1','2','3','4','5','6','7','8','9']
cnt =[0]*10
for m in g:
    for i in range(10):
        if m==chk[i]:
            cnt[i] +=1
print(*cnt, sep='\n')