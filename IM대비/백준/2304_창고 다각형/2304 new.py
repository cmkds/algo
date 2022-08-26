import sys

sys.stdin = open('input.txt')


N = int(input())
gidoongLst = [list(map(int, input().split())) for _ in range(N)]

gidoongLst.sort(key=lambda a: a[0])

a=0
maxgidoongIdx =0
for idx, gidoong in enumerate(gidoongLst):
   if a < gidoong[1]:
       a = gidoong[1]
       maxgidoongIdx = idx


leftChkLst = []
tmp = 0
for idx, giddong in enumerate(gidoongLst):
    if idx > maxgidoongIdx:
        break
    if tmp < giddong[1]:
        tmp = giddong[1]
        leftChkLst.append(giddong)

rightChkLst = []
tmp = 0
for i in range(len(gidoongLst)-1, maxgidoongIdx-1, -1):
    if tmp < gidoongLst[i][1]:
        tmp = gidoongLst[i][1]
        rightChkLst.append(gidoongLst[i])

cnt = 0
for i in range(len(leftChkLst)-1):
    cnt += leftChkLst[i][1] * ( leftChkLst[i+1][0]-leftChkLst[i][0])

print(leftChkLst)

for i in range(len(rightChkLst)-1):
    cnt += rightChkLst[i][1] * (rightChkLst[i][0]-rightChkLst[i+1][0])

print(rightChkLst)

cnt += leftChkLst[-1][1]

print(cnt)
