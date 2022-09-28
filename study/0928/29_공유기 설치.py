'''
5 3
1
2
8
4
9
'''
N, C = map(int,input().split())

lst = list(int(input()) for _ in range(N))

print(lst)
lst.sort()
print(lst)

##공유기를 탐색할 거리를 시작과 끝값의 중간값으로
##이진탐색하는 솔루션

start = lst[0]
end = lst[-1]
res = 0

while 1:
    mid = (start+end) // 2  ###
