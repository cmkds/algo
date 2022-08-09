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

    #리스트에서 최대값 찾는 함수와 최소값 찾는 함수를 이용하려 차이를 출력.
    print(f'#{test} {maxn(lst)-minn(lst)}')