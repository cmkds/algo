import sys
import copy
sys.stdin = open('input.txt')

testNum = int(input())
for test in range(testNum):
    a = int(input())

    def jump(a,tmpLst,chk):
        global lst
        if a < 0:
            return
        elif a==0:
            b = copy.deepcopy(tmpLst)
            if not b in lst:
                lst.append(b)
        else:
            for i in range(3,0,-1):
                if chk > i:
                    continue
                tmpLst[i-1] += 1
                chk =i-1
                jump(a-i,tmpLst,chk)
                tmpLst[i-1] -= 1



    ####1은 1   1개
    ####2는 1+1, 2   2개
    ####3은 1 1 1 , 1 2, 3 /   3개

    ########완전탐색. [0,0,0] 하고

    tmpLst=[0,0,0]
    lst = []

    k = jump(a,tmpLst,3)


    print(len(lst))