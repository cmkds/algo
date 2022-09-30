#단순 풀이
# x, y, w, h = map(int,input().split())
#
# #가로 계산
# garo = min(w-x,x-0)
# #세로 계산
# sero = min(h-y,y-0)
#
# print(min(garo,sero))

#최적화 1
#garo ,sero 구분안하고 한번에 min에 넣기. x-0, y-0은 계산할 필요없이 x,y 에 넣는다.

x, y, w, h = map(int, input().split())

print(min(w-x,h-y,x,y))