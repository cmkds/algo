###인덱스 에러 나고 망한 풀이.

K, N = map(int, input().split())

lst = [int(input()) for _ in range(K)]

minX = 0
maxX = max(lst)

# print(lst)
chk = 0
a = maxX
while a:
    a //= 2
    chk += 1

resLst = []
cnt = 0
middle = maxX
for _ in range(chk):
    cnt = 0
    for i in lst:
        cnt += i // middle
    resLst.append((cnt,middle))
    # print(cnt, K)
    if cnt > N:
        minX = middle
    else:
        maxX = middle
    # print(middle)
    middle = (minX + maxX) // 2
resLst.sort()
for i in range(len(resLst)):
    if resLst[i][0] >= N and resLst[i][0] < resLst[i+1][0]:
        print(resLst[i][1])
        break
print(resLst)
# print(middle)
