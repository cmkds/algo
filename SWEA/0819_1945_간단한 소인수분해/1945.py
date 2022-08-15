import sys

sys.stdin = open('input.txt')

testNum = int(input())
for test in range(1, testNum+1):
    num = int(input())

    cnt2 = 0
    while num % 2 == 0:
        num //= 2
        cnt2 += 1

    cnt3 = 0
    while num % 3 == 0:
        num //= 3
        cnt3 += 1

    cnt5 = 0
    while num % 5 == 0:
        num //= 5
        cnt5 += 1

    cnt7 = 0
    while num % 7 == 0:
        num //= 7
        cnt7 += 1

    cnt11 = 0
    while num % 11 == 0:
        num //= 11
        cnt11 += 1

    print(f'#{test} {cnt2} {cnt3} {cnt5} {cnt7} {cnt11}')