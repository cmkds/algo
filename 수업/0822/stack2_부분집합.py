def f(i, N):
    global answer
    global cnt
    cnt +=1
    if i == N:          ##채울칸의 인덱스 번호와 채울 칸수가 같아지면 종료 할거다.

        # print(bit)      ##bit 부분집합 출력

        s = 0
        for i in range(N):

            if bit[i]:      ##bit[i]가 1이면
                s += A[i]
                #print

        if s == 10:
            answer += 1     ##부분집합의 합이 10인 경우의수
            for i in range(N):
                if bit[i]:
                    print(A[i], end= ' ')
            print()
    else:
        candidate = [0, 1]
        for x in candidate:
            bit[i] = x
            f(i+1, N)

        # bit[i] = 1      ## A[i] 가 부분집합에 포함
        # f(i+1, N)
        # bit[i] = 0
        # f(i+1, N)


A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*10

answer = 0
cnt = 0

f(0,10)
print(answer, cnt)