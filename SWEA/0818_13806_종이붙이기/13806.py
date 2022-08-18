import sys

sys.stdin = open('input.txt')

lst = [1]
###########리스트에 바로 값저장해서 쓰는 버전으로 풀어보기
testNum = int(input())
for test in range(1, testNum+1):
    N = int(input())//10

    ###범위가 벗어나서 오류 뜨면 계산하고
    ##범위 안벗어나서 오류 안뜨면 있는 값을 집어넣음.

    #길이 만큼 반복
    for i in range(N):
    #리스트에 있을때 아무것도 안함
        try :
            lst[i] is not None
    #리스트에 없을때 채워 넣음

        #짝수일때

        #홀수일때