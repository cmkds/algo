import sys

sys.stdin = open('input.txt')

planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

t = int(input())
for _ in range(t):
    case, length = input().split()
    nums = list(input().split())
    idx = sorted([planet.index(i) for i in nums])
    print(idx)
    res = [planet[i] for i in idx]
    print(case)
    print(*res)