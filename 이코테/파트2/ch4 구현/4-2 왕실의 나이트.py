import sys
sys.stdin = open('4-2.txt')

### 현재 나이트의
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) +1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8방향 이동 여부 확인
res = 0
for step in steps:
    #이동 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        res += 1

print(res)