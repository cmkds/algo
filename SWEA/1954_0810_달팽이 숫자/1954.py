import sys

sys.stdin = open('input.txt')

testNum = int(input())


for test in range(1, testNum+1):
    N  = int(input())
    #N은 2번 이동할때 마다 1을 줄일 것이고
    # 전체리스트 길이를 저장하는 listLen 변수를 만들었다.
    listLen = N

    #N*N 배열을 0으로 초기화한다.
    lst= [[0]*N for _ in range(N)]

    #number는 이동할때 마다 숫자가 하나씩 커지면서
    number = 1
    cnt = 0

    # N 난 2번이동할때마다 -1

### N이 0이 될때까지 while문을 돌린다. N이 5라면 한줄씩 추가할 때마다. 5 4 4 3 3 2 2 1 1 0 이렇게 줄어든다.
    while N > 0 :

        ###0으로 초기화 한 배열에 값을 넣는다. N만큼 한번 하고 N을 -1  그다음부턴 2번 움직이고 -1 0이될때까지
        ##########N이 0될때까지 무한반복

        #cnt는 1바퀴 돌때 마다 +1 되면서
        #움직일 갈 칸수를 조절하고 첫 위치를 잡아준다.

        #N만큼 오른쪽으로 움직이는 코드. N이 5라면 5칸 3칸 1칸 이만큼 이동한다. 4칸 2칸
        for i in range(cnt, listLen-cnt):
            lst[cnt][i]= number
            number +=1
        else :
            N -= 1
            if N == 0:
                break
            # cnt +=1

        #-1하고 아래쪽  현재 N은 2

        for i in range(cnt +1, listLen-cnt):
            lst[i][listLen-cnt-1]= number
            number +=1

        # 그대로 왼쪽  현재 N=2 cnt=0

        for i in range(listLen-cnt-1, cnt, -1):
            lst[listLen-cnt-1][i-1] = number
            number += 1
        else:
            N -= 1
            if N == 0:
                break

        #-1하고 위쪽 현재 N=1 cnt =0

        for i in range(listLen - cnt -1, cnt + 1,-1):
            lst[i-1][cnt] = number

            number += 1
        else:
            cnt +=1

    print(f'#{test}')
    for ls in lst:
        print(' '.join(map(str,ls)))