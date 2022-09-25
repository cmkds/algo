import sys
sys.stdin = open('14074.txt')

def twoJinHeap(i):
    global last
    last +=1
    node.append(i)

    chk = last
    while chk // 2:
        if node[chk] < node[chk//2]:          #부모가 더 크면
            node[chk] , node[chk//2] = node[chk//2], node[chk]
            chk //= 2
        else:
            break

testNum = int(input())

for test in range(1, 1 + testNum):
    N = int(input())
    lst = list(map(int,input().split()))

    ##현재 맨뒤칸을 알려줄 변수를 만들어 줘야함.
    ##숫자가 들어오면 맨뒤칸에 넣어주고
    ##부모값이랑 비교하면서 부모값이랑 비교하면서 확인합니다.
    last = 0
    node = [0]

    for i in lst:
        twoJinHeap(i)
    # print(node)

    # print(node[last//2])
    cnt = 0
    while last:
        last //= 2
        cnt += node[last]

    print(f'#{test} {cnt}')