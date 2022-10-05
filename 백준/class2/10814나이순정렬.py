import sys

n = int(input())

lst = [ sys.stdin.readline().split() for _ in range(n)]

for i in range(n):
    lst[i][0] = int(lst[i][0])

# lst.sort(key=lambda x: x[1])
lst.sort(key=lambda x: x[0])
for i in range(n):
    print(lst[i][0], lst[i][1])