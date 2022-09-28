import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        if a == end:
            print(f'#{test} {visited[end]}')
            break
        for nextA in (a - 1, a + 1, a * 2, a - 10):
            if 0 <= nextA <= 10 ** 6 and not visited[nextA]:
                visited[nextA] = visited[a] + 1
                q.append(nextA)

testNum = int(input())

for test in range(1,1+testNum):
    start, end = map(int, input().split())
    visited = [0] * (10 ** 6 + 1)
    bfs()