n, m = map(int, input().split())

lst = [input() for _ in range(n)]
checkLst = []
# print(lst)
for i in range(n-7):
    for j in range(m-7):
        chk1 = 0
        chk2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if lst[a][b] != 'W':
                        chk1 += 1
                    if lst[a][b] != 'B':
                        chk2 += 1
                else:
                    if lst[a][b] != 'B':
                        chk1 += 1
                    if lst[a][b] != 'W':
                        chk2 += 1
        checkLst.append(chk1)
        checkLst.append(chk2)

# print(checkLst)
print(min(checkLst))