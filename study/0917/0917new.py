import sys

sys.stdin = open('input.txt')
a = int(input())

if a <= 6:
    ansLst =[0,1,2,3,4,5,7]
    print(ansLst[a], end='')
else:
    cnt = 0
    x, y = divmod(a, 3)
    # cnt += (x - 2) * 2 + 3
    cnt += (x - 1) * 3 + 1
    if y == 2:
        cnt += 1
    z = a//2
    cnt += z+1

    print(cnt%1000000, end='')

#1 - 1
#2 - 2, 1 1  = 2
#3  3, 2 1 , 1 1 1       3
#4  3 1, 2 2, 2 1 1, 1 1 1 1      3몫 3, 2 몫 1
#5  3 2, 3 1 1, 2 2 1, 2 1 1 1 , 1 1 1 1 1    5
#6  3 3  2 2 2       7

#1  1
#2  2
#3  3
#4  4
#5  5
#6  7

#7  7
#8  9
#9  10
#10 11
#11 12
#12 14
#13 14
#14 16