import sys

sys.stdin = open('input.txt')

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

cnt = 0

for i in lst:  #리스트를 돌리고

    for a in range(-4,1):  ##왼쪽에서 4번째 칸부터 제자리까지 확인
        tmpCnt = 0
        for b in range(5):  ## 우측으로 5칸 확인
            if i+a+b in lst:
                tmpCnt +=1
        if tmpCnt > cnt:
            cnt = tmpCnt
print(5-cnt)