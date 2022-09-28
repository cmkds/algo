import copy

N = int(input())
start = [1,2,3,4,5,6,7,8,9]
if N ==1:
    print(9)
else:
    lst =[]
    for i in start:
        a = i * 10 + i + 1
        b = i * 10 + i - 1
        if (a% 100)//10 == 1:
            lst.append(a)

        elif a %10 !=0:
            lst.append(a)
        if (b% 100)//10 == 1:
            lst.append(b)
        elif b %10 !=0:
            lst.append(b)

    # print(lst)

    while lst[0] <= 10**(N-1):
        newLst = []
        for i in lst:
            a = i * 10 + (i%10) + 1
            b = i * 10 + (i%10) - 1
            if (a % 100) // 10 == 1:
                newLst.append(a)
            elif a % 100 == 99:
                pass

            elif a % 10 != 0:
                newLst.append(a)
            if (b % 100) // 10 == 1:
                newLst.append(b)
            elif b % 100 == 99:
                pass

            elif b % 10 != 0:
                newLst.append(b)
        lst=[]
        # print(newLst)
        lst = copy.deepcopy(newLst)

    print(len(lst)%1000000000)