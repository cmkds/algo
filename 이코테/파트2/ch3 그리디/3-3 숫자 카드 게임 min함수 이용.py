import sys

sys.stdin = open('3-3input.txt')

testNum = int(input())
for test in range(testNum):

    n, m = map(int, input().split())

    result = 0
    for i in range(n):
        data  = list(map(int, input().split()))
        print(data)
        min_value = min(data)
        result = max(result, min_value)
    print(result)