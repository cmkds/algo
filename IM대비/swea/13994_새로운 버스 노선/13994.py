import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1,testNum+1):

    N = int(input())

    busLst = [list(map(int,input().split())) for _ in range(N)]
    staLst = [0] *1001

    for bus in busLst:
        if bus[0] == 1:                             #일반버스 다돔
            for i in range(bus[1],bus[2]+1):
                staLst[i] += 1
        elif bus[0] == 2:                           #급행버스
            for i in range(bus[1],bus[2]+1,2):      #2칸씩돌고
                staLst[i] += 1
            if (bus[1]+bus[2]) % 2 ==1:             #홀짝이나 짝홀인 경우 마지막 정거장 체크
                staLst[bus[2]] += 1
        elif bus[0] ==3:                                       #광역버스
            if bus[1] % 2 == 0:                     #짝수인경우 4칸씩
                for i in range(bus[1], bus[2]):
                    if i == bus[1]:                 #첫 정류장 가고
                        staLst[i] += 1
                    elif i % 4 == 0 :               #4의배수 정류장.
                        staLst[i] += 1
                staLst[bus[2]] += 1                 #마지막 정류장.

            else:                                   #홀수인경우
                for i in range(bus[1], bus[2]):
                    if i == bus[1]:                 #첫 정류장.
                        staLst[i] += 1
                        continue
                    if i % 10 == 0:                 #10의 배수이면 패스
                        continue
                    if i % 3 == 0:                #3의 배수일때 거침.
                        staLst[i] += 1

                staLst[bus[2]] += 1                 #마지막 정류장


    print(f'#{test} {max(staLst)}')