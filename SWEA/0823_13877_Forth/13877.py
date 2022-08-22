import sys

sys.stdin = open('input.txt')
##########이거 틀림 안쓸거임. 구글참고한 코드임. 오리지널 버전이 내가 푼거임
###isdigit() 함수로 숫자 구분하고
###try 짧게 정리

testnum = int(input())

for test in range(1, testnum+1):
    hoowiLst = list(input().split())      ##str로 받을때는 굳이 map 안써도되는거 확인하자

    newStack =[]                        ##후위 계산할 때 사용 할 newStack

    errorCheck = 1                      ##출력은 위한 에러체크 기본값 True

    for cha in hoowiLst:

        if cha.isdigit():
            newStack.append(cha)

        else:
            try:
                a = int(newStack.pop())
                b = int(newStack.pop())

                if cha == '*':
                   newStack.append(b * a)

                elif cha == '+':
                   newStack.append(b + a)

                elif cha == '-':
                   newStack.append(b - a)

                elif cha == '/':
                   newStack.append(b // a)

            except:
                 errorCheck = 0              #에러시 false
                 break
            print(newStack)
    print(newStack)
    if errorCheck and len(newStack) ==1:
        print(f'#{test} {newStack[0]}')
    else:
        print(f'#{test} error')