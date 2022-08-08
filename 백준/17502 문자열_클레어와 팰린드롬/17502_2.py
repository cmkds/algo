import sys
sys.stdin = open('input.txt')

num = int(input())
# 홀수일때 짝수 일때 상관없이 나누기 2한 몫만큼만
# 가면 된다.
str = input()

print(num, str)
for idx in range(1 , (num//2)+1):
    while True:
        if str[idx-1] == str[num-idx]:
            break
        elif str[idx-1] == '?' and str[num-idx] == '?':
            str[idx-1] , str[num-idx] = 'a'
            break
        elif str[idx-1] == '?':
            str[idx - 1] = str[num-idx]
            break
        elif str[num-idx] == '?':
            str[num - idx] = str[idx - 1]
            break

print(str)
## str은 변경이 안됨 망했음.