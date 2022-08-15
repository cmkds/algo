import sys

sys.stdin = open('input.txt')


testNum = int(input())

for test in range(1, testNum+1):
    A, B = input().split()

    a = len(A)  #A의 원본 길이를 저장할 변수

    C = A.split(B)  ##C는 A에서 B가 제거된 리스트

    C = ''.join(C)  #C를 다시 문자열로 만들어준다.

    b = 0  ##스플릿 회수를 담은 변수 b

    if len(B) != 0:
        b = (a-len(C))//len(B)  #split 전후 길이를 비교후 B의 길이로 나눠주면 split횟수

    c = len(''.join(C))   ##split 다하고 남은 배열의 길이

    print(f'#{test} {b + c}')  #cnt와 더해주고 출력한다.

