import sys

sys.stdin = open('input.txt')


testNum = int(input())
#기본 풀이

for test in range(1, testNum+1):
    str1 = input()
    str2 = input() #둘다 str값으로 받고
    cnt = 0
    for s2 in range(len(str2)-len(str1)+1):  #문자열길이 - 찾을문자열길이 +1
        tmp = 0
        for s1 in range(len(str1)):      #찾을 문자열길이 만큼 이동시키면서
            if str1[s1] == str2[s2+s1]:   # 시작점이 같을때 tmp를 올리면서 비교
                tmp += 1
            else:
                tmp = 0
            if tmp == len(str1):         #tmp가 찾을문자열 길이와 같으면 cnt +1
                cnt += 1
    print(f'#{test} {cnt}')




