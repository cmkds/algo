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
            if not stack:      #####비어있을때를 추가!
                break
            elif stack[-1] == '{':
                stack.pop()
            else:
                break
        elif i == ')':
            if not stack:      #####비어있을때를 추가!
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                break
    else:
        if not stack:
            res = 1
    print(f'#{test} {res}')
