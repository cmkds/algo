import sys
sys.stdin = open('input.txt')

def giri(byun,loc):
    if byun==1:
        return loc
    elif byun == 2:
        return x+y+x-loc
    elif byun == 3:
        return x+y+x+y-loc
    else:
        return x + loc

x, y = map(int,input().split())
num = int(input())

sLst =[]

for i in range(num):
    byun, loc = map(int,input().split())
    sLst.append(giri(byun,loc))

myB, myLoc = map(int,input().split())
myGiri = giri(myB,myLoc)

chongGiri = x*2+y*2    #전체 길이 #2x+2y

res = 0
for sGiri in sLst:
    res += min(abs(myGiri-sGiri),  chongGiri-abs(myGiri-sGiri)) #정방향 빼기 정방향 # 반대 방향
print(res)

