import sys

sys.stdin = open('3.txt')

m = input()

if len(m) == 1:  ##문자열이 1개주어질때
    print('0')
else:
    cnt0 = 0
    cnt1 = 0

    if m[0] == '0':
        cnt0 += 1
    else:
        cnt1 += 1

    #숫자가 바뀔때 계산해줘서. 처리가 더 깔끔.
    for i in range(len(m)-1):
        if m[i] != m[i+1]:
            if m[i+1] == '0':
                cnt0 += 1
            else:
                cnt1 += 1


    print(min(cnt0,cnt1))