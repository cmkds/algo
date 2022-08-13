import sys

sys.stdin = open('input.txt')

test = int(input())
for _ in range(test):
    k = int(input())
    n = int(input())
# k =2   n =3
lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
total = 0
for i in range(k): #2
   #1층
   #재귀? 층수는 재귀
   #호수는 for문
    for j in range(1,n+1): # 1~3
        # total += lst[j]
        total += lst[j-i]
    print(total)
