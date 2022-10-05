from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int,input().split())

q = deque()
for i in range(1,n+1):
    q.append(str(i))

lst =[]
cnt = 1
while q:
    if cnt % k:
        q.append(q.popleft())
    else:
        lst.append(q.popleft())
    cnt +=1
print(f'<{", ".join(lst)}>')

