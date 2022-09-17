###한개의 회의실
###N개의 회의에 대하여 회의실 사용표를 만든다

## 각 회의 I에 대해 시작시간, 끝나는 시간
## 회의가 겹치지 않게하면서 사용할 수 있는 최대 회의
### 회의는 한번 시작하면 중간에 중단 될수없다.
##시작시간과 끝나는시간이같을수있다.

#첫째줄
##회의수 1<=N<= 100,000
#둘째줄 ~~N+1
##회의 정보  . 회의시작시간, 끝나는 시간 2n31-1 보다 작거나 같은 자연수 혹은 0

####첫째줄을 정렬하면
N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
print(time)
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
print(time)
last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j
print(time)

print(conut)
