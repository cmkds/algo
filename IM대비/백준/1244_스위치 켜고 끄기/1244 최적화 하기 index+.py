import sys

sys.stdin = open('input.txt')


def change(a):            ### 0이면 1로 1이면 0으로 바꾸는 함수
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
    if gender == 1 :
       for i in range(bunho, Num+1, bunho):
           change(i-1)

    else:
        change(bunho-1)
        i = 1
        while bunho-i-1 >= 0 and bunho+i-1 <= Num-1:
            if lst[bunho - i - 1]  == lst[bunho + i - 1 ]:
                change(bunho - i - 1)
                change(bunho + i - 1)
                i += 1
            else:
                break


for i in range(1,Num+1):
    print(lst[i-1], end = " ")
    if i % 20 == 0:
        print()

#슬라이싱으로 출력하기
#for i in range(0, Num, 20):
#    print(*lst[i:i+20])

