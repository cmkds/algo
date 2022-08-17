from pprint import pprint
import sys
sys.stdin = open(input.txt)
# input=
#     7 7  #노드의 수 / 간선의 수
#     0 1
#     0 2
#     1 3
#     1 4
#     2 4
#     3 5
#     5 6
# 노드 : 점 / edge : 선
num_node, num_edge = map(int,input().split())


#1
lst = [[0]*7 for _ in range(7)]  #연결 리스트 방식

for _ in range(7):
    s, e = map(int,input().split())
    lst[s][e] = 1
    lst[e][s] = 1

#2
lst = [[] for _ in range(7)]

for _ in range(7):    #인덱스가 키고 값이 value인 딕셔너리와 비슷하다
    s, e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)

#3
dic = dict()
for _ in range(7):
    s, e = map(int,input().split())

    if dic[s]:
        dic[s].append(e)
    else:
        dic[s] =[e]

    dic[s] = dic.get(s, []) + [e]

#4

dic = dict()
from collections import defaultdict
dic_lst = defaultdict(list)
for _ in range(7):
    s, e = map(int,input().split())

    #1
    if dic[s]:
        dic[s].append(e)
    else:
        dic[s] =[e]

    #2
    dic[s] = dic.get(s, []) + [e]

    #3
    dic_lst[s].append(e)