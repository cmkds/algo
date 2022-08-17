import sys

sys.stdin = open('input.txt')


testNum = int(input())
for test in range(1, testNum+1):
    N = int(input())//10
    res = 1

    for i in range(1,N//2+1):
        res += (2**i)*

