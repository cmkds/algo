import sys
sys.stdin = open('input.txt')

for test in range(10):
    x = int(input())
    lst = list(map(int, input().split()))
    total = 0

    for lstIdx in range(2, x-2):
        cnt = 0
        a = lst[lstIdx]
        while a > lst[lstIdx-1] and a > lst[lstIdx-2] and a > lst[lstIdx+1] and a > lst[lstIdx+2]:
            cnt +=1
            a -=1
        total += cnt

    print(f'#{test+1} {total}')


