import sys
sys.stdin = open('input.txt')

testcase = int(input())
for test in range(testcase):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    T_item = [0 for _ in range(N + 1)]
    T_left = [0 for _ in range(N + 1)]
    T_right = [0 for _ in range(N + 1)]

    for n in range(1, N + 1):
        T_item[n] = lst[n]
        if N >= 2 * n:
            T_left[n] = 2 * n
        if N >= 2 * n + 1:
            T_right[n] = 2 * n + 1
    #    print(T_item)
    #    print(T_left)
    #    print(T_right)

    for i in range(1, N + 1):
        if T_left[i] or T_right[i]:
            if T_item[i] > T_item[2 * i]:
                t = T_item[i]
                l = T_item[2 * i]
                T_item[i] = l
                T_item[2 * i] = t
            if 2 * i + 1 <= N:
                if T_item[i] > T_item[2 * i + 1]:
                    t = T_item[i]
                    r = T_item[2 * i + 1]
                    T_item[i] = r
                    T_item[2 * i + 1] = t
    print(T_item)

    result = 0

    n = N // 2
    while n > 0:
        result += T_item[n]
        n = n // 2

    print(f'#{test + 1} {result}')