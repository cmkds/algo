import sys

sys.stdin = open('input.txt')
#############pop을쓰니가 짧고 효율적인데 시간 초과가 뜬다. 그래서
# list를 뒤집은다음에 역으로 팝을쓰는 사기적인방법
#pop은 뒤에서부터 계산한다고 하니깐

testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = lst[::-1]
    cnt = 0
    while 1:
        tmp = lst.pop()   #뒤집은 리스트 맨뒤에꺼 pop으로 빼서 계산한다.
        if not lst:
            break
        if tmp < max(lst):
            cnt += max(lst)-tmp

    print(f'#{test} {cnt}')