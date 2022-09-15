import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

setLst = sorted(list(set(lst)))

dic = {}

for i in range(len(setLst)):
    dic[setLst[i]] = i

for i in lst:
    print(dic[i], end=' ')