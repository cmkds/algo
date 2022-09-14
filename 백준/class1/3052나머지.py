lst = [int(input()) for _ in range(10)]

chkLst = [0]*42

for i in lst:
    chkLst[i%42] += 1

cnt = 0
for i in chkLst:
    if i:
        cnt +=1
print(cnt)