import sys

sys.stdin = open('input.txt')


#리스트에서 가장 큰값
def maxn(lst):
    maxNum = lst[0]
    for tmp in lst:
        if tmp > maxNum:
            maxNum = tmp
    return maxNum

#리스트에서 가장 작은값.
def minn(lst):
    minNum = lst[0]
    for tmp in lst:
        if tmp < minNum:
            minNum = tmp
    return minNum

#test 변수 1부터 받으려고 1,11
for test in range(1,11):
    #dump 횟수
    dumpNum = int(input())
    lst = list(map(int, input().split()))
    # print(dumpNum, lst)

    ##덤프 횟수
    for _ in range(dumpNum):
        #list에서 최소값을 구해주는 함수에 lst를 넣어서
        #최소값 찾음
        minNum = minn(lst)
        #list에서 최대값을 구해주는 함수에 lst를 넣어서
        #최대값 찾음
        maxNum = maxn(lst)

        for idx, ls in enumerate(lst):  ###덤프때 1개뺄것
            if ls == maxNum:  #lst 에서 maxNum과 같은게 나올 때 -1 해줘서 빼줌
                lst[idx] -= 1
                break
        for idx, ls in enumerate(lst):  ###마찬가지로 minNum과 같은게 나올때 +1해서 넣어줌
            if ls == minNum:
                lst[idx] += 1
                break

    #모든 덤프를 완료한후 다시. 리스트에서 최대값과 최소값을 찾아 그 차이를 출력.
    print(f'#{test} {maxn(lst)-minn(lst)}')
