import sys
from collections import deque

sys.stdin = open('input.txt')

##테스트 케이스가 몇개 인지 모르니깐
#나중에 수정해 일단 10개로
while True:
    try:
        Test = int(input())
        lst = list(map(int,input().split()))

        q = deque()         ##사용할 큐 생성

        #lst를 순회하면서 q에 값넣기  append()
        # for num in lst:
        #     q.append(num)
        # print(q)

        ###리스트 한번에 큐에 넣기 extend()
        q.extend(lst)

        i = 1
        while True:
            if i ==6:
                i =1

            #q에서 값을 빼고
            tmp = q.popleft()

            #그 값에 1빼고 #여기서 값이 0보다 작아진다면 0으로 넣고 밑에 break
            newNum = tmp - i

            #다시 집어 넣기
            if newNum > 0:
                q.append(newNum)

            else:
                q.append(0)
                break

            i += 1
        print(f'#{Test}', end =' ')
        print(*q)

    except EOFError:
        break



