import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    last += 1
    heap[last] = n

    c = last
    p = c//2
    while p and heap[p] > heap[c]:      ##루트노드 이거나 부모가 더 작으면 멈춤
        heap[p], heap[c] = heap[c], heap[p]
        c = p                           ##부모 노드의 위치로 옮기고
        p = c//2                        ##부모 노드의 위치를 찾음

testNum = int(input())

for test in range(1,testNum+1):
    n = int(input())
    lst = list(map(int,input().split()))
    heap = [0] * (n+1)                  ##힙리스트를 노드수보다 1크게 생성해준다. 인덱스를 노드번호로 쓰기 위해
    last = 0
    for i in lst:
        enq(i)
                                        ##노드 입력과 정렬이 끝나면 last는 노드의 끝 번호.
    cnt = 0
    while last:                         ##마지막 노드 부터
        cnt += heap[last//2]            ##부모노드를 탐색하면서 루트노드까지 합을 더함
        last //= 2
    print(heap)
    print(f'#{test} {cnt}')

