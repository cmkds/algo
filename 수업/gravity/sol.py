#gravity
#1. 떨어지는건 사실 오른쪽
#2. 오른쪽에서 나보다 작은 녀석의 수를 셈
# 나의 낙차

#전체의 낙차 중에 가장 큰것을 고르자.
import sys
sys.stdin = open('input.txt')

lst = list(map(int, input().split()))

# for i in lst:
#     print(i)

res = 0
for idx in range(len(lst)-1):
    value = lst[idx]
# 나보다 작은 박스 무더기의 수를 세야해요.
    cnt = 0 # 하나씩 더해줄껍니다
# 나보다 오른쪽에 있는
    for right_idx in range(idx+1, len(lst)):
        if value > lst[right_idx]:  # 숫자를 1 더해줄게
            cnt += 1
    #1
    if cnt > res:
        res = cnt

    #2
    #res = max(res,cnt)

    #3
    #res = res if res > cnt else cnt




# 1.인덱스 활용 => 인덱스를 가지고 원소를 활용
# 2.원소 활용
print(res)