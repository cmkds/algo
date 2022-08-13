from itertools import combinations
import sys

sys.stdin = open('input.txt')

#부분집합 구하기.
#합이 100인 부분집합 찾기.

##반복문으로 부분집합 구하기

lst = []
for _ in range(9):
    lst.append(int(input()))



#########1 itertools 라이브러리의 combinations 메서드 이용
#from itertools import combinations 를 맨위에 적어주고
#combinations(리스트이름, 부분집합크기)
res1 = []
res1 = res1+list(combinations(lst,7))




############################
#2. 단순 반목문과 배열
res2 = [[]]

for i in lst:
    # print([i])
    ###현재 res2의 길이만큼 안쪽 for문을 계속 돌린다.
    size = len(res2)
    ###for문이 돌면서 lst의 원소 순서대로 쌓인다.
    #ex 1,2,3 의 부분집합이
    #처음엔 []만있고 1이 추가된 배열이 하나씩생성되고 2가추가된 배열이 하나씩 생성되고......
    for j in range(size):
        res2.append(res2[j]+[i])
print(res2)
for lst in res2:
    if len(lst) ==7 and sum(lst)==100:
        a = sorted(lst)

# for b in a:
#     print(b)