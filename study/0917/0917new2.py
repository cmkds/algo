import sys

sys.stdin = open('input.txt')
testNum = int(input())
for test in range(testNum):
    a = int(input())
    ###6으로 나눈 몫 +1 / 몫 *3
    if a%6 == 0:
        res = (((a // 6) + 1) * ((a // 6) * 3))+1
    else:
        # print(a//6+1)
        # print((a // 6) * 3)
        res = ((a // 6) +1 ) * (((a // 6) * 3)+a%6)
    print(res)
