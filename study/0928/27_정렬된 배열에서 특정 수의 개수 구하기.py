def ejin(s, e, key, cnt):
    mid =(s+e)//2
    if cnt == over:         ##탐색시작할때마다 오르는 cnt가 over랑 같으면 재귀가 멈추도록 설정
        return
    if lst[mid] == key:     ##찾으면 해당 인덱스 리턴
        return mid
    elif lst[mid] < key:        ##작으면 왼쪽 범위로 탐색
        e = mid
        ejin(s,e,key,cnt+1)
    else:                       ##크면 오른쪽 범위로 탐색
        s = mid
        ejin(s,e,key,cnt+1)


N, key = map(int,input().split())

lst = list(map(int,input().split()))

s = 0
e = N-1
over = 0      ##값이 없을시 반복문 빠져나가는거 설정을 어캐하지?
              ##고민하다가 전체리스트 길이 6칸이면 2^3승이하
              ##15칸이면 2^4승 이하 만 탐색하면 되므로
              ##리스트가 2의 몇승 싸이즈 인지 구하고 over에 넣었습니다.
while N:
    N //= 2
    over += 1

a = ejin(s, e, key, 0)
# print(a)
l, r = a, a
if a:                   ###리턴된 인덱스에서 왼쪽 오른쪽 탐색하면서 다른 값이 나올때까지 탐색하고
                        ###값은 값이면 cnt를 +1
    cnt = 1
    while lst[l-1] == lst[a]:
        l -= 1
        cnt += 1
    while lst[r+1] == lst[a]:
        r += 1
        cnt += 1
    print(cnt)

else:           ##리턴값이 없을시 -1
    print(-1)