import sys
sys.stdin = open('input.txt')

def dfs(x,y,tmpLst,chk):
    global zhoaPyoLst
    # print(tmpLst)
    x = tmpLst[-1][0]
    y = tmpLst[-1][1]
    if len(tmpLst) == 7:
        print(tmpLst)
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
            dfs(ny, nx, tmpLst, chk)
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
        chk = 0
        tmpLst = []
        tmpLst.append((x,y))
        # print(tmpLst)
        dfs(x,y,tmpLst,chk)
aLst = list(zhoaPyoLst)

# print(len(zhoaPyoLst))
# print(aLst)
#16488


testNum = int(input())

for test in range(1,1+testNum):
    lst = [list(map(int,input().split())) for _ in range(4)]
    # print(lst)
    resLst = set()

    #16488
    tmp = ''
    for i in range(16488):
        for j in range(7):
            a, b = aLst[i][j]
            tmp += str(lst[a][b])
        resLst.add(tmp)
        tmp=''
    print(resLst)
    print(f'#{test} {len(resLst)}')
