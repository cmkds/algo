import sys

sys.stdin = open('3.txt')

######가면서 0일때 +
###### 1일때 +
# ### 둘중 작은거 답

m = input()


if len(m) == 1:  ##문자열이 1개주어질때
    print('0')
else:
    cnt0 = 0
    cnt1 = 0
    tmpM = m[0]
    for i in range(1, len(m)):
        if m[i] == tmpM:  ##이전 값과 같으면
            continue
        else:

            if m[i] == '1':
                tmpM = '1'
                cnt0 +=1
            else:
                tmpM = '0'
                cnt1 += 1
    if m[-1] == m[-2]:
        if m[-1] == '0':
            cnt0 += 1
        else:
            cnt1 += 1

    if m[-1] != m[-2]:
        if m[-1] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
    # print((cnt0,cnt1))
    print(min(cnt0,cnt1))