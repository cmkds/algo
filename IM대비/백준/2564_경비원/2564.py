import sys

sys.stdin = open('input.txt')

x, y = map(int,input().split())

num = int(input())

sLst =[[],[],[],[],[]]

for i in range(num):
    byun, loc = map(int,input().split())
    sLst[byun].append(loc)

myB, myLoc = map(int,input().split())

#print(storeLst)         #[[], [4], [8], [2], []]
#print(myByun,myLoc)     # 2 3

#x 축길이 #y축 길이

cnt =0
for b in range(1,5):    #b =  변
    for sLoc in sLst[b]:

        #같은 라인 일때
        if b == myB:
            cnt += abs(myLoc-sLoc)

        #마주 보는 라인 일때 #1,2 일때
        elif b + myB == 3:
            if myLoc+sLoc >= x:     #합친게 더 클때
                cnt += (x*2) - (myLoc + sLoc)
            else:
                cnt += myLoc + sLoc
            cnt += y

        # 마주 보는 라인 일때 3, 4 일때
        elif b + myB ==7:
            if myLoc+sLoc >= y:     #합친게 더 클때
                cnt += (y*2) - (myLoc + sLoc)
            else:
                cnt += myLoc + sLoc
            cnt += x

        #옆라인 일때  #1 00  #2 0y  #3 00 #4 x0
        else:
            if b + myB == 4:
                cnt += sLoc + myLoc

            elif b + myB == 6:   # b + myB ==5:
                cnt +=

            else:
                if b + myB ==5:

                else:  # b+ myB == 6

