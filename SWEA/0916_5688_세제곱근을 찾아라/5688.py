import sys
sys.stdin = open('input.txt')

# 1~10n3
#
# 3~6
#
# 6~9
#
# 9~12
#
# 12~15
#
# 15~18
#
# 홀수, 짝수일때 판별하는 함수 각각 만들기.
def hol(n,a,b):
    if a==0:
        for i in range(10**(a//3),10**(b//3),2):
            if n == i**3:
                return i
        return -1
    else:
        for i in range(10**(a//3)+1,10**(b//3),2):
            if n == i**3:
                return i
        return -1

def ZZAKKKKKKK(n,a,b):
    if a==0:
        for i in range(10**(a//3)+1,10**(b//3)+1,2):
            if n == i**3:
                return i
        return -1
    else:
        for i in range(10**(a//3),10**(b//3)+1,2):
            if n == i**3:
                return i
        return -1



testNum = int(input())

for test in range(1, 1+testNum):
    n = int(input())
    if n % 2 :  #홀수 일 때
        if 10**0<= n <10**3:
            res = hol(n,0,3)
        elif 10**3 <= n < 10**6:
            res = hol(n,3,6)
        elif 10 ** 6 <= n < 10 ** 9:
            res = hol(n,6,9)
        elif 10 ** 9 <= n < 10 ** 12:
            res = hol(n,9,12)
        elif 10 ** 12 <= n < 10 ** 15:
            res = hol(n,12,15)
        elif 10 ** 15 <= n <= 10 ** 18:
            res = hol(n,15,18)


    else:
        if 10**0<= n <10**3:
            res = ZZAKKKKKKK(n,0,3)
        elif 10**3 <= n < 10**6:
            res = ZZAKKKKKKK(n,3,6)
        elif 10 ** 6 <= n < 10 ** 9:
            res = ZZAKKKKKKK(n,6,9)
        elif 10 ** 9 <= n < 10 ** 12:
            res = ZZAKKKKKKK(n,9,12)
        elif 10 ** 12 <= n < 10 ** 15:
            res = ZZAKKKKKKK(n,12,15)
        elif 10 ** 15 <= n <= 10 ** 18:
            res = ZZAKKKKKKK(n,15,18)

    print(f'#{test} {res}')