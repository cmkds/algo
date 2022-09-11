import sys
sys.stdin = open('1.txt')

n = int(input())
lst = list(map(int,input().split()))
lst.sort()

cnt = 0              #총 그룹의수
tmpCnt = 0          #현재 그룹에 포함된 모험가의 수

#print(lst)
for i in lst:
    tmpCnt += 1     #현재 그룹에 해당 모험가를 포함시키기
    if tmpCnt >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        cnt += 1
        tmpCnt = 0

print(cnt)