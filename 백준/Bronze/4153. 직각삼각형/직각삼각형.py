import sys
input = sys.stdin.readline
while True:
    a,b,c = map(int,input().split())
    if a+b+c==0:
        break
    lst =[]
    lst.append(a**2)
    lst.append(b**2)
    lst.append(c**2)
    lst.sort()
    # print(lst)
    if lst[0]+lst[1]==lst[2]:
        print('right')
    else:
        print('wrong')