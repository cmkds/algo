import sys

sys.stdin = open('input.txt')

# N = 리스트 길이
# M = 구간의 길이
def sumn(N,M,lst):
    newlst = []             #구간의 합들을 담을 빈 리스트 생성

                            #리스트길이가 10이고 구간의 길이가 3이라할때
                            #3이 10안에 8번들어갈수 있다. 변수로 나타내면 N-M+1
    for idx in range(N-M+1):

        tmpTotal = 0                  #구간의 숫자 총합을 넣기 위한 tmpTotal 변수


        for i in range(idx, idx+M):   #구간길이만큼 리스트를 돌리면서 tmpTotal에 값추가.
            tmpTotal += lst[i]

        newlst.append(tmpTotal)       #추가된 구간합을 리스트에 담음
    return newlst

#리스트에서 가장 큰 값을 찾는 함수
def maxn(newlst):
    maxNum =newlst[0]
    for tmp in newlst:
        if tmp > maxNum:
            maxNum = tmp
    return maxNum

#리스트에서 가장 작은 값을 찾는 함수
def minn(newlst):
    minNum =newlst[0]
    for tmp in newlst:
        if tmp < minNum:
            minNum = tmp
    return minNum


testNum = int(input())

for test in range(1, testNum+1):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    newlst = sumn(N,M,lst)

#리스트 최대값과 최소값의 차이를 출력
    print(f'#{test} {maxn(newlst)-minn(newlst)}')
