import sys

sys.stdin = open('input.txt')


def maxn(lst):
    maxNum = lst[0]
    for tmp in lst:
        if tmp > maxNum:
            maxNum = tmp
    return maxNum


def minn(lst):
    minNum = lst[0]
    for tmp in lst:
        if tmp < minNum:
            minNum = tmp
    return minNum


for test in range(1,11):
    dumpNum = int(input())
    lst = list(map(int, input().split()))
    # print(dumpNum, lst)

    ##덤프 횟수
    for _ in range(dumpNum):
        minNum = minn(lst)
        # print(minNum)
        maxNum = maxn(lst)
        # print(maxNum)
        for idx, ls in enumerate(lst):  ###덤프때 1개뺄것
            if ls == maxNum:
                lst[idx] -= 1
                break
        for idx, ls in enumerate(lst):  ###덤프때 1개뺄것
            if ls == minNum:
                lst[idx] += 1
                break

    print(f'#{test} {maxn(lst)-minn(lst)}')
