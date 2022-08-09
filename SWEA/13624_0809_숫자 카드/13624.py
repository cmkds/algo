import sys

sys.stdin = open('input.txt')

#lst안의 값의 갯수를 세서 값과 갯수를 튜플로 리턴하는 함수
def cntnum(a, lst):
    cnt = 0
    for tmp in lst:
        if a == tmp:
            cnt += 1
    return a, cnt,

## 카드갯수를 나타내는 cards 변수와 그 숫자를 num
#우선 리스트 첫인덱스의 값으로 초기화
def maxcard(newlst):

    cards = newlst[0][1]
    num = newlst[0][0]
    #리스트를 돌리면서
    for tup in newlst:
        #cards개수가 크거나 같을때, 값이 같은데 숫자가 더 클 수 도있으니
        if tup[1] >= cards:
            #일때 숫자가 더 크다면
            # 그 값으로 cards와 num에 할당
            if tup[0]> num:
                cards = tup[1]
                num = tup[0]
    return num, cards

testNum = int(input())

#띄어쓰기가 없는 입력값이라 split() 없이 받음
for test in range(1, testNum+1):
    num = int(input())
    lst = list(map(int, input()))


    newlst =[cntnum(a,lst) for a in lst]
    #print(newlst)
    #[(4, 1), (9, 2), (6, 1), (7, 1), (9, 2)]
    #[(0, 1), (8, 1), (2, 1), (7, 1), (1, 1)]
    #[(7, 3), (7, 3), (9, 2), (7, 3), (9, 2), (4, 2), (6, 1), (5, 1), (4, 2), (3, 1)]
    # print(maxcard(newlst))

    print(f'#{test} {maxcard(newlst)[0]} {maxcard(newlst)[1]}')

