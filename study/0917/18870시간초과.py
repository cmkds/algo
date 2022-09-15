import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

setLst = sorted(list(set(lst)))

for i in lst:
    print(setLst.index(i), end=' ')