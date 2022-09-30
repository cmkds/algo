
# 줄이 증가할때마다 6+12+18 가되고
## 그 줄만큼의 값을 구하면된다.
## 껍데기의 갯수를 카운트 해주고 껍데기 레벨수 *6을 계속 해주면 된다.
n = int(input())
cnt = 1
case = 1
while n > cnt:
    cnt += case*6
    case +=1
print(case)