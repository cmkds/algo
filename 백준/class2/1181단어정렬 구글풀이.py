import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(input().strip())


lst = list(set(lst))
# print(lst)
lst.sort()
lst.sort(key=len)

print(*lst, sep='\n')