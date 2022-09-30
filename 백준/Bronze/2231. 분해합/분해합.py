n = int(input())

for i in range(n+1):
    N = list(str(i))
    res = i
    for j in N:
        res += int(j)
    if res == n:
        break
if i == n:
    print(0)
else:
    print(i)