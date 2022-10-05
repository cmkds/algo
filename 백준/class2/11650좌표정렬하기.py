import sys
input = sys.stdin.readline

n = int(input())

lst = [ list(map(int,input().split())) for _ in range(n)]

lst.sort(key=lambda x:x[1])
lst.sort(key=lambda x:x[0])

for a, b in lst:
    print(a,b)