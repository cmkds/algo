import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    moonjang = input()
    stack = []

    res = 0
    for i in moonjang:
        if i == '{':
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                res =0
                break
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                res =0
                break
    else:   ##for문이 break 안됐을 때만 써야함 else를 안걸어서 틀린듯?
        if not stack:
            res = 1
    print(f'#{test} {res}')
