import sys
sys.stdin = open('input.txt')

testNum = int(input())


for test in range(1,1+testNum):

    N, M = map(int,input().split())
    #N은 세로길이 1~2000
    #M은 가로길이 26(1), 50(2), 126(5), 250, 250, 500


    ##숫자 14칸 단위로 가져오기
