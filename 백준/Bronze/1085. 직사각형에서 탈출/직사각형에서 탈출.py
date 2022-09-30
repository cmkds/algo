x, y, w, h = map(int,input().split())

#가로 계산
garo = min(w-x,x-0)
#세로 계산
sero = min(h-y,y-0)

print(min(garo,sero))