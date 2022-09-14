import copy
import sys
sys.setrecursionlimit(10000)
a = int(input())

def jump(a,tmpLst):
    global lst
    if a < 0:
        return
    elif a==0:
        b = copy.deepcopy(tmpLst)
        if not b in lst:
            lst.append(b)
    else:
        for i in range(1,4):
            tmpLst[i-1] += 1
            jump(a-i,tmpLst)
            tmpLst[i-1] -= 1



####1은 1   1개
####2는 1+1, 2   2개
####3은 1 1 1 , 1 2, 3 /   3개

########완전탐색. [0,0,0] 하고

tmpLst=[0,0,0]
lst = []

k = jump(a,tmpLst)


print(len(lst))