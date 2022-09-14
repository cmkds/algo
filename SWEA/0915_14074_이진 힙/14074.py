import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c//2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

testNum = int(input())

for test in range(1,testNum+1):
    n = int(input())
    lst = list(map(int,input().split()))
    heap = [0] * 501
    last = 0
    for i in lst:
        enq(i)

    cnt = 0
    while last:
        cnt += heap[last//2]
        last //= 2
    print(f'#{test} {cnt}')

