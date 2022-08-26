import sys

sys.stdin = open('input.txt')


def change(a):            ### 0이면 1로 1이면 0으로 바꾸는 함수
    if lst[a] == 0:
        lst[a] =1
    else:
        lst[a] = 0

def searchBaesoo(a, Num):   ### 배수를 찾는 함수
    b = a    #a의 처음 값을 담을 변수
    while a-1< Num:
        change(a-1)
        a += b

def findDaeChing(a, Num): ###대칭인지 확인하는 함수
    change(a-1)
    i = 1
    while a-i-1>=0 and a+i-1<=Num-1:
        if lst[a-i-1] == lst[a+i-1]:
            change(a-i-1)
            change(a+i-1)
            i +=1
        else:
            break



Num = int(input())   ##리스트 길이

lst = list(map(int,input().split()))  ##리스트 받기

switchS = int(input())   ##스위치 할 횟수

for _ in range(switchS):
    gender, bunho = map(int,input().split())
    if gender ==1: #남자일때는 배수를 찾는 함수로
        searchBaesoo(bunho,Num)
    else:   #여자일때는 대칭을 찾는 함수로
        findDaeChing(bunho, Num)

for i in range(1,Num+1):
    print(lst[i-1], end = " ")
    if i % 20 == 0 :
        print()


