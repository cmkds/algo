import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    N, Q = map(int, input().split())  #N은 상자수 , Q는 작업수
    lst = [list(map(int, input().split())) for i in range(Q)] #[[1,3][2,4]]
    newLst = [0]*N


    #작업수만큼 for문 돌리기
    for a in range(Q):  #a+1의 값으로 값을 바꿔줘야함
        for b in range(lst[a][0]-1,lst[a][1]): # 1~3  # 0 1 2 이니깐 실제론 1,2,3번 박스 맞음
            newLst[b] = a+1    #newLst b위치에 a+1 값 할당

    print(f"#{test} {' '.join(map(str,newLst))}")

