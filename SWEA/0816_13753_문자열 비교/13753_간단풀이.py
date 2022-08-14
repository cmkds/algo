import sys

sys.stdin = open('input.txt')

#간단 풀이
testNum = int(input())

for test in range(1, testNum+1):
    str1 = input()
    str2 = input()
    cnt = 0
    if str1 in str2:
        cnt = 1
        break
    print(f'#{test} {cnt}')




