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

testNum = int(input())

for test in range(1,testNum+1):
    num = int(input())
    lst = list(map(int, input().split()))

    print(f'#{test} {maxn(lst)-minn(lst)}')