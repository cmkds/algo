import sys

sys.stdin = open('input.txt')


def cntnum(a, lst):
    cnt = 0
    for tmp in lst:
        if a == tmp:
            cnt += 1
    return a, cnt,

def maxcard(newlst):
    cards = newlst[0][1]
    num = newlst[0][0]
    for tup in newlst:
        if tup[1] >= cards:
            if tup[0]> num:
                cards = tup[1]
                num = tup[0]
    return num, cards

testNum = int(input())

for test in range(1, testNum+1):
    num = int(input())
    lst = list(map(int, input()))

    newlst =[cntnum(a,lst) for a in lst]
    # print(newlst)
    # print(maxcard(newlst))

    print(f'#{test} {maxcard(newlst)[0]} {maxcard(newlst)[1]}')

