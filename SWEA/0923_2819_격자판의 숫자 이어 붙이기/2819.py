def dfs(x,y,tmpLst,chk):
    while True:
        if chk == 6:
            zhoaPyoLst.append(tmpLst)
            print(zhoaPyoLst)
            tmpLst = [x, y]
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if N > nx >= 0 and N > ny >= 0:
                chk += 1
                tmpLst.append([ny, nx])
                dfs(ny, nx, tmpLst, chk)
                tmpLst.pop()
            else:
                continue



###4*4배열 dfs 좌표 모두 뽑기.




dx = [0,0,-1,1]
dy = [-1,1,0,0]

N = 4
lst = [[0]*N for _ in range(4)]
print(lst)

zhoaPyoLst = []
tmpLst=[]
for x in range(N):
    for y in range(N):
        chk = 0
        tmpLst.append([x,y])
        while True:
            if chk == 6:
                zhoaPyoLst.append(tmpLst)
                print(zhoaPyoLst)
                tmpLst = [x, y]
                break
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if N>nx>=0 and N>ny>=0:
                    chk +=1
                    tmpLst.append([ny, nx])
                    x = nx
                    y = ny
                else:
                    continue

print(zhoaPyoLst)