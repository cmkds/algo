n = input()
ans =''
while n != '0':
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            ans = 'no'
            break
    else:
        ans = 'yes'

    print(ans)

    n = input()