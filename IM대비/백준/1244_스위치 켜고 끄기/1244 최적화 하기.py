import sys

sys.stdin = open('input.txt')


def change01(a):            ### 0이면 1로 1이면 0으로 바꾸는 함수
    if lst[a] == 0:
        lst[a] =1
    else:
        lst[a] = 0
    return


Num = int(input())   ##리스트 길이

lst = list(map(int,input().split()))  ##리스트 받기

switchS = int(input())   ##스위치 할 횟수

for _ in range(switchS):
    gender, bunho = map(int,input().split())
    if gender ==1 :
       for i in range(bunho, Num, bunho):
           change01(i-1)
       print(lst)
    else:
        change01(bunho - 1)
        for k in range(Num//2):
            if bunho - i - 1 < 0 or bunho + i - 1 > Num-1:
                 break
            if lst[bunho - i - 1] == lst[bunho + i - 1]:
                change01(bunho - i - 1)
                change01(bunho + i - 1)

            else:
                break


for i in range(Num):
    print(lst[i], end = " ")
    if i+1 % 20 == 0:
        print()


##20개씩 리스트 분할 하기
# n= 20
# res = [lst[i * n:(i+1)*n] for i in range((len(lst)-1+n)//n)]
#
# for a in range(len(lst)//20+1):
#     print(*res[a])