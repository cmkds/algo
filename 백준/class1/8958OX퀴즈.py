n = int(input())


for i in range(n):
    st = input()

    cnt = 0
    chk = 0
    for m in st:
        if m =='O':
            chk += 1
            cnt += chk
        else:
            chk =0
    print(cnt)
