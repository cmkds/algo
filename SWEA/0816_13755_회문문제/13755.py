# lst2= [[0]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         lst2[i][j] = lst[j][i]
#
# for i in range(n):
#     for j in range(n):
#         if i>j:
#             lst[i][j] = lst[j][i]

import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1, testNum+1):
    N , M = map(int, input().split())
    #N*N 문자열
    #M길이의 회문 찾기
    #N 이용해서 인풋 받으면서 리스트 만들기
    ##이중 배열 리스트로 만들기
    lst = [list(input()) for i in range(N)]

    #리스트의 길이에서 N-M만큼 회문 비교 해야함

    #####가로행 확인

    #전체 배열 돌리고
    for i in range(N): #전체 배열 돌리고
        for r in range(N-M+1):  #배열 길이에서 회문 문자열길이 +1 만큼 전진 # ex) 10칸에서 7단어 회문이면 4번 조사
            chk = 0
            for m in range(M//2): ## 회문길이의 반절만큼 전진하면서 회문을 확인 #회문은 반절만 조사하면된다
                                        # //2로 나누어주면 짝수 홀수 둘다 상관없이 커버됨.
                ##여기에 회문 확인하는 코드
                if lst[i][r+m] == lst[i][M-1-m+r]: # r+m = r위치에서 m만큼씩 이동하면서 확인
                                                  # M-1+r  = N-(N-M) 전체길이-(회문길이와 전체의 차이) + r만큼이동
                                                            # -m 으로 빼면서 회문 끝에서 부터 이동.
                    chk +=1                     #일치할때 chk를 1올려줌
                else :
                    chk = 0

                if chk == (M//2): #체크가 회문크기에 도달했을때  #회문 길이의 절반만큼 chk가 찍히면 그건 회문
                    #정답 회문을 담을 res 변수
                    res = ''
                    for k in range(M):
                        res = res+ lst[i][r+m-(M//2)+1+k]   #(현재위치는 r+m(회문의 중간이므로) r+m위치에서
                                                            #회문의 절반만큼(M//2) 돌아간다
                                                            #+1은 list인덱스가 0부터 시작하는것으로 인한
                                                            #계산 보정
                                                            #하고 회문길이인 M만큼 돌리면서 res에 값을 넣는다.


    ########세로열 확인
    #리스트 행열 바꾼다.
    lst = list(zip(*lst))
    for i in range(N):

        for r in range(N-M+1):
            chk = 0
            for m in range(M//2):
                if lst[i][r+m]== lst[i][M-1-m+r]:
                    chk +=1
                else :
                    chk = 0

                if chk == (M//2):
                    res = ''
                    for k in range(M):
                        res = res+ lst[i][r+m-(M//2)+1+k]

    print(f'#{test} {res}')