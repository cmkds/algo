import sys
# sys.setrecursionlimit(10**7)


def dfs(x,y,tmpLst):
    global zhoaPyoLst
    # print(tmpLst)
    if len(tmpLst) == 7:
        # print(tmpLst)
        zhoaPyoLst.add(tuple(tmpLst))
        # print(zhoaPyoLst)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if N > nx >= 0 and N > ny >= 0:
            # print(tmpLst)
            # print(ny, nx, 'ny-nx')
            tmpLst.append((ny, nx))
            # print('###', tmpLst)
            dfs(ny, nx, tmpLst)
            tmpLst.pop()
        # else:
        #     return

###4*4배열 dfs 좌표 모두 뽑기.


dx = [0,0,-1,1]
dy = [-1,1,0,0]

N = 4
lst = [[0]*N for _ in range(4)]
# print(lst)

zhoaPyoLst = set()

for x in range(N):
    for y in range(N):
        tmpLst = []
        tmpLst.append((x,y))
        # print(tmpLst)
        dfs(x,y,tmpLst)
aLst = list(zhoaPyoLst)

# print(len(zhoaPyoLst))
print(aLst)