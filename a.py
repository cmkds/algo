lst = [1,2,3]
res =[[]]

for i in lst:
    size = len(res)

    for j in range(size):
        res.append(res[j]+[i])
print(res)

for i in range(1,4):
    for j in range(1,4):
        if i != j:
            for k in range(1,4):
                if i!=k and j !=k:
                    print(i,j,k)

n = 10
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            print(i,j,k)