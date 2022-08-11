import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(f'#{test}', end=' ')
    M = 10
    #10개제한인지모르고 while문썼는데 for문이 더 좋았을 듯
    while M > 0 :
        tmpMax = lst[0]
        maxIdx = 0
        for idx, num in enumerate(lst):
            if num > tmpMax:
                tmpMax = num
                maxIdx = idx

        if M == 1:
            print(lst.pop(maxIdx), end='')
        else :
            print(lst.pop(maxIdx), end=' ')


        M -= 1

        tmpMin = lst[0]
        minIdx = 0
        for idx, num in enumerate(lst):
            if num < tmpMin:
                tmpMin =num
                minIdx = idx
        if M == 1:
            print(lst.pop(minIdx), end='')
        else:
            print(lst.pop(minIdx), end=' ')
        M -= 1
    print()
