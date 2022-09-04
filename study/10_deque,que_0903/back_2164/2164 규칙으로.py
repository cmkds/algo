import sys

sys.stdin = open('input.txt')

N = int(input())
k = 1

while True:
    if N == 1 or N == 2:
        print(N)
        break
    k *= 2

    if k >= N/2:
        print((N - k) * 2)
        break