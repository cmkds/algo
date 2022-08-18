import sys

sys.stdin = open('input.txt')
####일단 pass인지 확인하고 dp 구현해보자.
def a(N):
    if N ==2:
        return 3
    elif N ==1:
        return 1
    else:
        return 2 * a(N-2) + a(N-1)


testNum = int(input())
for test in range(1, testNum+1):
    N = int(input())//10

    print(f'#{test} {a(N)}')
