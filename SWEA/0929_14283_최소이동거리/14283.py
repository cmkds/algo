import sys
sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1,1+testNum):
    N, E = map(int,input().split()) #N = 마지막 노드, E = 도로의 개수

    lst = []      # 노드의 크기 만큼 리스트 만들기
    for _ in range(N):
        lst.append([])
    for i in range(E):
        s,e,w = map(int, input().split())
        lst[s].append((e,w))
    print(lst)