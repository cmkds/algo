import sys

sys.stdin = open('input.txt')

def a(k,n):
    if k == 0 :
        return n
    elif n == 1:
        return 1

    return a(k-1,n)+a(k,n-1)

test = int(input())
for _ in range(test):
    k = int(input())
    n = int(input())


    print(a(k,n))
