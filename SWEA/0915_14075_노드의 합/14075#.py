import sys
sys.stdin = open('input.txt')

testNum = int(input())

for test in range(1,1+testNum):

    N, M, L = map(int,input().split())      # N노드의 개수, M 리프 노드의 개수, L 값을 출력할 노드

    lst = [0]*(N+1)
    for i in range(M):
        idx, num = map(int,input().split()) #주어진 노드의 번호와 값을 받아서
        lst[idx]=num                        #저장

    for i in range(N-M,0,-1):               #뒤쪽(리프노드)부터 루트 노드로 계산
        try :                               #자식들의 합을 부모 노드에 저장
            lst[i] = lst[i*2]+lst[i*2+1]
        except IndexError:                  #우측 자식이 없는 경우 좌측자식만 더 해줌
            lst[i] = lst[i*2]
    print(f'#{test} {lst[L]}')