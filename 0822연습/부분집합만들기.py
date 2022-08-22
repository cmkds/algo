lst = [1,2,3]

newLst = [[]]

for i in lst:
    size = len(newLst)

    for j in range(size):
        newLst.append(newLst[j]+[i])
print(newLst)