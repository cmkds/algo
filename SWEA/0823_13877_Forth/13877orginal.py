import sys

sys.stdin = open('input.txt')

testnum = int(input())

for test in range(1, testnum+1):
    hoowiLst = list(map(str,input().split()))

    newStack =[]                    ##후위 계산할 때 사용 할 newStack

    errorCheck = 1                  ##출력은 위한 에러체크 기본값 True
    for cha in hoowiLst:

        try:
            if cha == '*':
               a = int(newStack.pop())
               b = int(newStack.pop())
               newStack.append(a * b)
            elif cha == '+':
               a = int(newStack.pop())
               b = int(newStack.pop())
               newStack.append(a + b)
            elif cha == '-':
               a = int(newStack.pop())
               b = int(newStack.pop())
               newStack.append(b - a)
            elif cha == '/':
               a = int(newStack.pop())
               b = int(newStack.pop())
               newStack.append(b // a)
            elif cha =='.':
                break
            else:
                newStack.append(int(cha))
        except:

            errorCheck = 0              #에러시 false
            break

    if errorCheck and len(newStack) == 1 :  ##리스트에 숫자가 더 많아서 찌꺼기가 있는 경우는 에러뜨도록 추가
        print(f'#{test} {newStack[0]}')
    else:
        print(f'#{test} error')