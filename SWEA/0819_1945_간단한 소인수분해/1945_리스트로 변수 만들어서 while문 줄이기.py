import sys

sys.stdin = open('input.txt')

testNum = int(input())
for test in range(1, testNum+1):
    num = int(input())
    lst = [2,3,5,7,11]
    cnt = [0,0,0,0,0]

    for i, n in enumerate(lst):
        while num % n ==0:
            num //= n
            cnt[i] += 1

    print(f'#{test} {cnt[0]} {cnt[1]} {cnt[2]} {cnt[3]} {cnt[4]}')