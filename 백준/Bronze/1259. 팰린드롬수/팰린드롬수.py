n = -1
ans =''
while 1:        #0이 아닐 때까지 while문 반복
    n = input()
    for i in range(len(n)//2):
        # print(n[i], n[-(i+1)])
        if n[i] != n[-(i+1)]:
            ans = 'no'
            break
    else:
        ans ='yes'
    if n != '0':
        print(ans)
    else:
        break