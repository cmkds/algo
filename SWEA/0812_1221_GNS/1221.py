import sys

sys.stdin = open('input.txt')

testNum = int(input())

for test in range(testNum):
    testShop , lenLst = list(map(str, input().split()))

    lst = list(map(str, input().split()))
    #리스트를 돌면서 문자열을 숫자로 전환하고

    for i, l in enumerate(lst):
        if l =='ZRO':
            lst[i] =0
        elif l =='ONE':
            lst[i] =1
        elif l =='TWO':
            lst[i] =2
        elif l =='THR':
            lst[i] =3
        elif l =='FOR':
            lst[i] =4
        elif l =='FIV':
            lst[i] =5
        elif l =='SIX':
            lst[i] =6
        elif l =='SVN':
            lst[i] =7
        elif l =='EGT':
            lst[i] =8
        elif l =='NIN':
            lst[i] =9

    lst.sort()

    for i, l in enumerate(lst):
        if l ==0:
            lst[i] ='ZRO'
        elif l ==1:
            lst[i] ='ONE'
        elif l ==2:
            lst[i] ='TWO'
        elif l ==3:
            lst[i] ='THR'
        elif l ==4:
            lst[i] ='FOR'
        elif l ==5:
            lst[i] ='FIV'
        elif l ==6:
            lst[i] ='SIX'
        elif l ==7:
            lst[i] ='SVN'
        elif l ==8:
            lst[i] ='EGT'
        elif l ==9:
            lst[i] ='NIN'
    #sort하고
    #다시 문자로 전환
    print(testShop)
    print(' '.join(lst))

