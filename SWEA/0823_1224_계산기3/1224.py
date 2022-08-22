import sys

sys.stdin = open('input.txt')

def isp(cha):
    if cha == '*':
        return 2
    elif cha == '+':
        return 1
    elif cha =='(':
        return 0
def icp(cha):
    if cha == '*':
        return 2
    elif cha == '+':
        return 1
    elif cha =='(':
        return 3


for test in range(1, 11):
    X = int(input())

    chars = input()

    ###############중위를 후위로 바꾸기#####################
    stackSign = []                        ##부호를 잠시 보관할 stack
    strHoowi = ''                       ##후위 모양을 담을 str 변수

    for cha in chars:
        if cha ==')':                           ###닫는 괄호가 나오면 여는 괄호가 나올때까지 stack에 pop한 값 넣기
            while True:
                a = stackSign.pop()
                if a != '(':
                    strHoowi += a
                else:                           ##여는 괄호 나오면 break
                    break

        elif cha == '*' or cha == '+' or cha =='(':
            if not stackSign:
                stackSign.append(cha)
            elif icp(cha) > isp(stackSign[-1]):           #stack top 이 더 작을 때.
                stackSign.append(cha)                     #스택에 추가
            else:
                while icp(cha) <= isp(stackSign[-1]):     ##stack top이 더 크거나 같을 때
                    strHoowi += stackSign.pop()         #top이 더 커지거나 stack이 빌때까지 pop

                    if not stackSign:                     #stack이 비면 while문을 종료시킨다.
                        break
                stackSign.append(cha)                     ###!! while문이  다돌면 cha를 스택에 추가시켜준다.
        else:
            strHoowi += cha
    else:                                       ###!! 마지막에 stackSign에 남아있는 기호도 전부 추가해 줘야한다.
        while stackSign:
            strHoowi += stackSign.pop()

    #####################################################

    ###strHoowi를 앞에서 부터 스택에 넣으며 후위 계산하기.

    newStack =[]                    ##후위 계산할 때 사용 할 newStack
    for cha in strHoowi:
        if cha == '*':
           newStack.append(int(newStack.pop()) * int(newStack.pop()))

        elif cha == '+':
           newStack.append(int(newStack.pop()) + int(newStack.pop()))
        else:
            newStack.append(int(cha))

    print(f'#{test} {newStack[0]}')
