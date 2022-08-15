import sys

sys.stdin = open('input.txt')

testNum = int(input())

##solution
###가장 큰값구하고 그값 인덱스 구하고 그 인덱스 왼쪽값 차 싹 더하고
### 그리고 다 제거
##가장 큰값의 인덱스가 0이면 해당인덱스 삭제, 리스트 길이가 1이 되면 정지.
for test in range(1, testNum+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0


    while lst:
        # if not lst:
        #     break
            
        tmp = max(lst)        #큰값 저장
        idx = lst.index(tmp)  #큰값 인덱스 저장

        if idx == 0:   ##가장 큰값의 idx가 0이면 해당 index 삭제하고 다시 돌림
            # lst.remove(tmp)
            lst.pop(0)
            # print(lst)
            continue
        for i in range(idx):  #### 가장큰값 왼쪽 값 차이 다더하고
            cnt += lst[idx]- lst[i]
        del lst[:idx+1]          #####처음 부터 큰값까지 다 제거






    print(f'#{test} {cnt}')