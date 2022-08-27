import sys
import copy

sys.stdin = open('input.txt')

def sideDice(start, Lst): #시작점 다이스 리스트를 받고
                               # 끝점과 사이드 리스트를 리턴해주는 함수
    diceLst = copy.deepcopy(Lst)
    startIdx = diceLst.index(start)
    if startIdx == 0:
        # endIdx = 5
        end = diceLst[5]
    elif startIdx == 1:
        # endIdx = 3
        end = diceLst[3]
    elif startIdx == 2:
        # endIdx = 4
        end = diceLst[4]
    elif startIdx == 3:
        # endIdx = 1
        end = diceLst[1]
    elif startIdx == 4:
        # endIdx = 4
        end = diceLst[2]
    elif startIdx == 5:
        end = diceLst[0]
    diceLst.pop(startIdx)
    diceLst.remove(end)

    return end, diceLst

dices = int(input())

lst = []
for dice in range(dices):
    lst.append(list(map(int,input().split())))

## 값으로 인덱스 찾기.
## 앞뒤를 튜플로 담을 리스트

maxSide = 0

for i in range(6):
    #첫주사위는 6면 다 돌린다.
    sideLst = []

    start = lst[0][i-1]
    end , tmpSideLst = sideDice(start, lst[0])
    sideLst.append(tmpSideLst)

    for j in range(1,dices):#남은 주사위 확인하고 옆면을 저장한다.
        end, tmpSideLst = sideDice(end,lst[j])
        sideLst.append(tmpSideLst)
    #print(sideLst)


    tmpMaxSide = 0
    for ls in sideLst:
        tmpMaxSide += max(ls)
    if tmpMaxSide > maxSide:
        maxSide = tmpMaxSide

print(maxSide)