import sys

sys.stdin = open('input.txt')


def aDP(N, dp):
    if dp[N] == -1:   ###dp가 -1이라면 아직 계산이 안됐따면
        dp[N] = 2 * aDP(N-2, dp) + aDP(N-1, dp) ##재귀를 돌려줌
                                        ###근데 dp를이용하면 재귀코드지만
                                        ##전값들은 다 들어있는 상태니깐
                                        ##딱한번 돌아감
                                        ##기존에 들어있는 값들로 계산되서
                                        ##메모리와 속도에서 엄청난
                                        ##이득을 가져옴.
    return dp[N]  ###값이있따면 그값을 씀. 바로 리턴해줌.


testNum = int(input())
for test in range(1, testNum+1):
    N = int(input())//10
    dp = [-1] * (N+1)  ###리스트 길이보다 +1로 만들어줌
                    ###why? 리스트는 0부턴데 경로는 1부터니깐
    #dp[0] = 0    ##이건 안넣어 놔도 될것같긴한데 일단 넣어둠
    dp[1] = 1    ### stop을 위한 시작값
    dp[2] = 3    ### stop을 위한 시작값
    print(f'#{test} {aDP(N,dp)}')
