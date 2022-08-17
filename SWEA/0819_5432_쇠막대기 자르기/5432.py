import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    lst = list(map(str, input()))

    stack = 0  ##현재 막대수를 담을 변수
    total = 0  ####잘려진 막대기 수를 담을 변수

    for i, a in enumerate(lst):

        if a == '(' :
            if lst[i+1] == '(':  # (( 인경우
                stack +=1
            else:   # ()인 경우 아무것도안하고 뒤쪽닫는 괄호에서 처리해준다.
                pass
        else: # )일경우
            if lst[i-1] =='(':   ## () 인경우 이거면 레이저
                total += stack      ##현재까지 막대기를 잘라서 더해준다.
            else:  # ))인경우  #막대가 종료되면 레이저로 잘린수 +1이므로 total에 +1 해준다.
                total += 1
                stack -= 1

    print(f'#{test} {total}')