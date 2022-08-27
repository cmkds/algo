import sys

sys.stdin = open('input.txt')


N = int(input())
gidoongLst = [list(map(int, input().split())) for _ in range(N)]

gidoongLst.sort(key=lambda a: a[0])           ### 기둥리스트 인덱스 순서대로 정렬  ###


########기둥 최대값 구하기
maxGidoong=0
for idx, gidoong in enumerate(gidoongLst):
   if maxGidoong < gidoong[1]:
       maxGidoong = gidoong[1]

########기둥 리스트 만들기
maxGidoongLst = []
for idx, gidoong in enumerate(gidoongLst):
    if maxGidoong == gidoong[1]:
        maxGidoongLst.append([idx, gidoong[1], gidoong[0]])

###########################################################

###왼쪽 시작 점부터 첫번째 최댓값까지 커지는 기둥의 인덱스와 높이를 저장
leftChkLst = []
tmp = 0
for idx, giddong in enumerate(gidoongLst):
    if idx > maxGidoongLst[0][2]:
        break
    if tmp < giddong[1]:
        tmp = giddong[1]
        leftChkLst.append(giddong)

###오른쪽 시작 점부터 마지막번째 최댓값까지 커지는 기둥의 인덱스와 높이를 저장
rightChkLst = []
tmp = 0
for i in range(len(gidoongLst)-1, maxGidoongLst[-1][0] -1, -1):
    if tmp < gidoongLst[i][1]:
        tmp = gidoongLst[i][1]
        rightChkLst.append(gidoongLst[i])

###최대값 왼쪽 카운트
cnt = 0
if len(leftChkLst) > 1:
    for i in range(len(leftChkLst)-1):
        cnt += leftChkLst[i][1] * ( leftChkLst[i+1][0]-leftChkLst[i][0])

###최대 값 오른쪽 카운트
if len(rightChkLst) > 1:
    for i in range(len(rightChkLst)-1):
        cnt += rightChkLst[i][1] * (rightChkLst[i][0]-rightChkLst[i+1][0])

###최대 높이 기둥 카운트
if len(maxGidoongLst)==1:
    cnt += maxGidoong
else:
    cnt += maxGidoong * (maxGidoongLst[-1][2] - maxGidoongLst[0][2]+1)
print(cnt)
