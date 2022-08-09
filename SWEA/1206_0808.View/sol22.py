import sys
sys.stdin = open('input.txt')

def my_max(a, b, c, d):
    tmp = a
    if tmp < b:
        tmp = b
    if tmp < b:
        tmp = b
    if tmp < c:
        tmp = c
    if tmp < d:
        tmp = d
    return tmp

for case in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    res = 0

#0,0 공간이 안주어진다면 이런식으로 사용하자.
    # lst = [0,0] + lst + [0,0]
    #
    # lst[0:0] = [0,0]
    # lst[n:n] = [0,0]


#나와 max값의 차이만큼 result에 더해주겠어.
    for i in range(2, n-2):
        near_max = my_max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])

        if  near_max < lst[i] :
            res += lst[i] - near_max
    print(res)



