import sys

sys.stdin = open('input.txt')


N = int(input())
gidoongLst = [list(map(int, input().split())) for _ in range(N)]


lst = [0]*1000
gidoongLst.sort(key=lambda a: a[0])
#print(gidoongLst)
for gidoong in gidoongLst:
    idx, h =gidoong[0], gidoong[1]
    lst.insert(idx, h)

#lst를 첫번째 인덱스로 정렬하기

# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
##가장 큰값과 인덱스 찾기
M = max(lst)
mIdx = lst.index(M)

#print(mIdx, M)
a=0
MaxgidoongIdx =0
for idx, gidoong in enumerate(gidoongLst):
   if a<gidoong[1]:
       a= gidoong[1]
       MaxgidoongIdx = idx
#print(MaxgidoongIdx)

leftChkLst = []
####중앙 기둥리스트를 찾았음. 여기서 왼쪽부터 크면 리스트에 인덱스랑 값을 저장.
tmp = 0
for idx, giddong in enumerate(gidoongLst):
    if idx > MaxgidoongIdx:
        break
    if tmp < giddong[1]:
        tmp = giddong[1]
        leftChkLst.append(giddong)

# rightChkLst = []
# for idx, giddong in enumerate(gidoongLst,-1):
#     if idx <= gidoongIdx:
#         break
#     if tmp < giddong[1]:
#         rightChkLst.append(giddong)
# print(leftChkLst)
# print(rightChkLst)

#print(gidoongLst)
#print(MaxgidoongIdx)
rightChkLst = []
####중앙 기둥리스트를 찾았음. 여기서 왼쪽부터 크면 리스트에 인덱스랑 값을 저장.
tmp = 0
for i in range(len(gidoongLst)-1, MaxgidoongIdx-1, -1):
    if tmp < gidoongLst[i][1]:
        tmp = gidoongLst[i][1]
        rightChkLst.append(gidoongLst[i])
#print(leftChkLst)
#print(rightChkLst)

###

###인덱스 왼쪽에서 값 찾기,  인덱스 오른쪽에서 값찾기.
###맥스값 찾기
cnt = 0
for i in range(len(leftChkLst)-1):
    cnt += leftChkLst[i][1] * ( leftChkLst[i+1][0]-leftChkLst[i][0])
#print(cnt)


for i in range(len(rightChkLst)-1):
    cnt += rightChkLst[i][1] * (rightChkLst[i][0]-rightChkLst[i+1][0])
#print(cnt)
cnt += M

print(cnt)
