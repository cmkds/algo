import sys

sys.stdin = open('input.txt')

testNum = int(input())


for test in range(1, testNum+1):
    N  = int(input())       #N은 2번 이동할때 마다 1을 줄일 것이고


    listLen = N             # 전체리스트 길이를 저장해두는는 listLen 변수


    lst= [[0]*N for _ in range(N)]      #N*N 배열을 0으로 초기화한다.

    #number는 이동할때 마다 숫자가 하나씩 커지면서
    number = 1
    cnt = 0            #cnt 변수는 1바퀴 돌때 마다 +1 되면서
                       #움직일 갈 칸수를 조절하고 시작 위치를 잡아준다

    while N > 0 :       ### N이 0이 될때까지 while문을 돌린다.

        #N만큼 오른쪽으로 움직이는 코드. N이 5라면 5칸 3칸 1칸 이만큼 이동한다.
        for i in range(cnt, listLen-cnt):
            lst[cnt][i]= number
            number +=1
        else :
            N -= 1
            if N == 0:
                break


        for i in range(cnt +1, listLen-cnt):
            lst[i][listLen-cnt-1]= number
            number +=1


        for i in range(listLen-cnt-1, cnt, -1):
            lst[listLen-cnt-1][i-1] = number
            number += 1
        else:
            N -= 1
            if N == 0:
                break

        for i in range(listLen - cnt -1, cnt + 1,-1):
            lst[i-1][cnt] = number

            number += 1
        else:
            cnt +=1


    print(f'#{test}')
    for ls in lst:
        print(' '.join(map(str,ls)))