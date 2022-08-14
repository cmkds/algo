import sys

sys.stdin = open('input.txt')

def a(k,n):
    lst = [[0] * n for _ in range(k+1)]
    # #lst[층][호
    # print(lst)
    if k == 0 :
        return n
    if n == 1:
        return 1
    # for i in range(n):
    #     a(0,n) = i
    # for i in range(k):
    #     lst[i][1] = 1
    return a(k-1,n)+a(k,n-1)

test = int(input())
for _ in range(test):
    k = int(input())
    n = int(input())
#층수는  k =2 호수는   n =3

# total = 0
# for i in range(k): #2
#    #1층
#    #재귀? 층수는 재귀
#    #호수는 for문
#     for j in range(1,n+1): # 1~3
#         # total += lst[j]
#         total += lst[j-i]
#     print(total)
    print(a(k,n))
