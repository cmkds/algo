import sys

sys.stdin = open('input.txt')

###스택 개념으로 풀이.

testNum = int(input())

for test in range(1, testNum+1):
    moonja10 = input()
    stack = []
    for moonja in moonja10:
        if not stack:
            stack.append(moonja)
        elif moonja == stack[-1] :
            stack.pop()
        else :
            stack.append(moonja)

    print(f'#{test} {len(stack)}')
