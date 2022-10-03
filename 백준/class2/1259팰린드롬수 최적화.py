import sys
input = sys.stdin.readline

n = input().strip()
ans = ''
while n != '0':
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            ans = 'no'
            break
    else:
        ans = 'yes'

    print(ans)

    n = input().strip()