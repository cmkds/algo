## 브루트 포스 알고리즘.
## 모든 경우의 수를 다 체크해 보는 방법.
## 보통 값이 1,000,000 이하 인 경우의 문제에서 사용 가능하다.
## 그보다 크면 브루트 포스로는 시간 초과 날 확률이 높다.


## 생성자가 없는 경우에는 0을 출력하는 것을 빼먹어서 틀렸다.
## 문제 잘 체크.

n = int(input())

for i in range(n+1):
    N = list(str(i))
    res = i
    for j in N:
        res += int(j)
    if res == n:
        break
if i == n:
    print(0)
else:
    print(i)

## 스트링으로 바꾸고 리스트에 넣고 int로 다시 바꾸고 합치는 과정
for i in range(n+1):
    N = list(str(i))
    res = i
    for j in N:
        res += int(j)
# 위 코드를
# 밑의 코드로 짧게 구현 할 수 있다.
# for 문 돌려서 나온 i 값을 str으로 바꾸고 map int를 해서 바로 리스트 형태로 만들어준다.
for i in range(n+1):
    res = i + sum(map(int, str(i)))


n = int(input())
res = 0
for i in range(n+1):
    tmp = i + sum(map(int, str(i)))

    if tmp == n:
        res = tmp
        break

print(res)