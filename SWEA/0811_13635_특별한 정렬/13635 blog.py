import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))

    print(f'#{test}', end=' ')


    for i in range(5):

        tmpMax = lst[0]
        maxIdx = 0
        for idx, num in enumerate(lst):
            if num > tmpMax:
                tmpMax = num
                maxIdx = idx

        print(lst.pop(maxIdx), end=' ')


        tmpMin = lst[0]
        minIdx = 0
        for idx, num in enumerate(lst):
            if num < tmpMin:
                tmpMin =num
                minIdx = idx
        if i == 4:
            print(lst.pop(minIdx), end='')
        else:
            print(lst.pop(minIdx), end=' ')

    print()
