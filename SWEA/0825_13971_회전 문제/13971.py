import sys
from collections import deque

sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1, testNum+1):
    N, M = map(int,input().split()) #N은 주어지는 숫자 M은 작업수

    q = deque(map(int,input().split()))   ##인풋 받으면서 한번에 데큐로 받기

    chk = M%N +1
    for _ in range(chk):
        a = q.popleft()
    print(f'#{test} {a}')
    