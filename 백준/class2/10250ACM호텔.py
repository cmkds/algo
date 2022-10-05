T = int(input())

for i in range(T):
    H, W, N = map(int,input().split())  #층수, 방수, 몇번째 손님
    if N%H:

        end = str(N // H + 1)
    else:
        end = str(N//H)

    if N%H:
        start = str(N % H)
    else:
        start = str(H)
    if len(end) ==1:
        end = '0' + end
    print(start+end)
