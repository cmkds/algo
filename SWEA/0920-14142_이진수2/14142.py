import sys
sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1,1+testNum):
    n = float(input())
#    k=0
    i=-1
    res =''
    while n:
       a, n = divmod(n, 2 ** i)
       res += str(int(a))
       # print(divmod(n,2**i))
       i -= 1

    if len(res)<=12:
        print(f'#{test} {res}')
    else:
        print(f'#{test} overflow')
