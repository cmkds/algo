import sys

sys.stdin = open('input.txt')

#보이어무어
def boyer(chk,str):
    reverseChk = list(reversed(chk))

    cnt = 0
    idx = len(chk)-1

    while cnt != len(chk) and idx < len(str):
        if str[idx] in reverseChk:
            if str[idx] == reverseChk[cnt]:  #역순chk랑 chk -1을 비교
                cnt +=1           #같으면 cnt +1
                idx -=1           #idx -1 하면서 역순 비교 while문돌면서 지속
                continue
            else:
                idx += reverseChk.index(str[idx])  #도중에 틀린걸 확인하면 온만큼 idx를 더해줌
                cnt = 0 #cnt는 초기화
        else:
            idx += len(chk) #chk 만큼 조사했을때 chk가 없으면 len만큼 점프
            cnt = 0
    if cnt == len(chk):
        return 1
    if idx == len(str):
        return 0



testNum = int(input())

for test in range(1, testNum+1):
    str1 = input()
    str2 = input()

    print(f'#{test} {boyer(str1,str2)}')




