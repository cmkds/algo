import sys
sys.stdin = open('input.txt')
from collections import defaultdict


def dijkstra(s):
    used = [s]
    distance = [float('inf') for _ in range(V+1)]
    distance[s] = 0

    for e, weight in lst[s]:
        distance[e] = weight

testNum = int(input())

for test in range(1,1+testNum):
    N, E = map(int,input().split()) #N = 마지막 노드, E = 도로의 개수

    lst = [[0]*(N+1) for _ in range(N+1)]      # 노드의 크기 만큼 리스트 만들기

    for i in range(E):
        s,e,w = map(int, input().split())
        lst[s][e] = w
    print(lst)

