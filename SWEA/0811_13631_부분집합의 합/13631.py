import sys

sys.stdin = open('input.txt')


arr = [1,2,3,4,5,6,7,8,9,10,11,12]

n = len(arr)
booBoonLst = []
for i in range(1<<n):
    booBoon = []
    for j in range(n):
        if i & (1<<j):
            booBoon.append(arr[j])
    booBoonLst.append(booBoon)

# print(booBoonLst)
# print(len(booBoonLst))



testNum = int(input())

for test in range(1, testNum+1):
    nums, chongHab = map(int, input().split())

    cnt = 0
    for lst in booBoonLst:
        if len(lst) == nums:
            if sum(lst) == chongHab:
                cnt +=1
    print(f'#{test} {cnt}')