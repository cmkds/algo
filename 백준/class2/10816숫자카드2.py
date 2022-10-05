N = int(input())
dic = {}
lst = input().split()
for i in lst:
    if i in dic:
    # if dic[i]:
        dic[i] += 1
    else:
        dic[i] = 1

k = int(input())
chkLst = input().split()

for i in chkLst:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end= ' ')