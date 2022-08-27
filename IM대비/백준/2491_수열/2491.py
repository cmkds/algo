import sys

sys.stdin = open('input.txt')

num = int(input())

lst = list(map(int,input().split()))

upCnt = 1
downCnt = 1
maxCnt = 1
for i in range(num-1):
    if lst[i] == lst[i+1]:
        upCnt +=1
        downCnt +=1
        if i == (num-2):
            if upCnt > maxCnt:
                maxCnt = upCnt
            if downCnt > maxCnt:
                maxCnt = downCnt

    elif lst[i] <= lst[i+1]:
        upCnt +=1
        if downCnt > maxCnt:
            maxCnt = downCnt
        downCnt = 1
        if i == (num - 2):
            if upCnt > maxCnt:
                maxCnt = upCnt
    else:
        downCnt +=1
        if upCnt > maxCnt:
            maxCnt = upCnt
        upCnt = 1
        if i == (num - 2):
            if downCnt > maxCnt:
                maxCnt = downCnt

print(maxCnt)