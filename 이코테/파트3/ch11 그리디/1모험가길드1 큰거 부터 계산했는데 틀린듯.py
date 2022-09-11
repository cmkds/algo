import sys
sys.stdin = open('1.txt')

n = int(input())
lst = list(map(int,input().split()))

lst.sort()
# print(lst)
#[1, 2, 2, 2, 3]
cnt = 0
while lst:
    a = lst.pop()
    for _ in range(a-1):
        lst.pop()
    cnt +=1
print(cnt)