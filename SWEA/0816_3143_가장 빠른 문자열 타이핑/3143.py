import sys

sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1, testNum+1):
    A, B = map(str, input().split())

    a = len(A)  #A의 원본 길이를 저장할 변수
    cnt = 0       ### split 될때마다 추가할 cnt

    while True:
        try:
            A = A.split(B, 1)   #1회 스플릿
            a -= len(B)         # a를 B의 길이 만큼 뺀다
            if a == len(A):     # 만약 a와 잘린 A가 같다면 cnt +1 다르다면 A에 B가 더이상 없어서 안짤린 것
                cnt += 1
        except AttributeError : #다를때 AttributeError가 뜨고 break 해준다
            break

    b = len(''.join(A))   ##split 다하고 남은 배열의 길이

    print(f'#{test} {b + cnt}')  #cnt와 더해주고 출력한다.

