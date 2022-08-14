import sys

sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1, testNum+1):
    # charsLst = list(input())
    # a = []
    # a.extend((input()))
    # b = input()
    # c = [*b]
    # print(c, check)
    chars = input()
    check = input()
    newChars = set(chars)

    cnt = 0
    for char in chars:
        tmp =0
        for chk in check:
            if chk == char:
                tmp +=1
        if tmp > cnt:
            cnt = tmp

    print(f'#{test} {cnt}')
