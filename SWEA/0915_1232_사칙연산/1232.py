import sys
sys.stdin = open('input.txt')

for test in range(1,11):
    N = int(input())
    lst = [0]+[list(input().split()) for _ in range(N)]

    for i in range(N,0,-1):
        try:
            lst[i][1] = int(lst[i][1])
        except ValueError:
            if lst[i][1] == '+':
                lst[i][1] = lst[int(lst[i][2])][1] + lst[int(lst[i][3])][1]
            elif lst[i][1] == '-':
                lst[i][1] = lst[int(lst[i][2])][1] - lst[int(lst[i][3])][1]
            elif lst[i][1] == '*':
                lst[i][1] = lst[int(lst[i][2])][1] * lst[int(lst[i][3])][1]
            else:
                lst[i][1] = lst[int(lst[i][2])][1] / lst[int(lst[i][3])][1]

    print(f'#{test} {int(lst[1][1])}')