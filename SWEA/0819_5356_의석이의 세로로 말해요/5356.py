import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):

    lst = [list(input()) for i in range(5)]
    maxLen = 0
    for i in lst:               ##배열중에서 제일 긴 배열로 for문돌릴길이를 정함.
        tmpLen = len(i)
        if tmpLen > maxLen:
            maxLen = tmpLen
    res = ''

    for i in range(maxLen):
        for j in range(5):
            try :
                res = res+lst[j][i]
            except IndexError:
                continue
    print(f'#{test} {res}')