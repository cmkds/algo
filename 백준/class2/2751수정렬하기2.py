import sys
input = sys.stdin.readline
n = int(input())
a =[]
for i in range(n):
    a.append(int(input()))
a.sort()
# print(a)
print(*a, sep='\n')