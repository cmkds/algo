import sys

sys.stdin = open('input.txt')
#Z collect page
def twojin(page, Z):
    l = 1
    r = page
    tmp= int((l+r)/2)
    cnt = 1
    while tmp != Z:

        if Z > tmp:
            l = tmp
        else:
            r = tmp
        tmp = int((l + r) / 2)
        cnt += 1
    return cnt


testNum = int(input())

for test in range(1, testNum+1):
    page, A, B = map(int, input().split())


    cntA = twojin(page,A)
    cntB = twojin(page,B)

    if cntA < cntB:
        print(f'#{test} A')
    elif cntA == cntB:
        print(f'#{test} 0')
    else :
        print(f'#{test} B')