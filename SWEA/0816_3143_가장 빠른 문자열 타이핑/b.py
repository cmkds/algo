import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    str1, str2 = input().split()
    idx = []
    total = len(str1)
    total_auto = len(str2)
    cnt = 0
    chk = 0
    while chk < total:
        if str2[0] == str1[chk]:
            idx.append(chk)
            chk += total_auto
            cnt += 1
        else :
            chk += 1
    cnt = 0
    for i in idx:
        if i + total_auto > total:
            break
        for j in range(total_auto):
            if str1[i+j] != str2[j]:
                break
        else:
            cnt += 1
    print(f'#{test_case} {total - cnt*(total_auto-1)}')