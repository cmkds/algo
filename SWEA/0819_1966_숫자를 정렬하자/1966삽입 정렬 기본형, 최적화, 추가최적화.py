import sys

sys.stdin = open('input.txt')
#삽입 정렬
###삽입정렬 기본형
def selectSort(lst):
    for end in range(1, len(lst)):  ##1부터 시작해서 리스트 길이만큼 밑의 for문 돌린다
        for i in range(end, 0, -1):   ###1  21  321 4321 54321 이렇게 돌아간다.
            if lst[i - 1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]


###삽입 정렬 최적화   ###실행시간을 늘어나고 메모리가 줄었음
def selectSort2(lst):
    for i in range(1, len(lst)):  ##1 2 3 4 5
        chk = i
        while chk>0 and lst[chk-1] > lst[chk]:              ###1 21 321 4321 54321 이렇게 돌아간다.
            lst[chk - 1], lst[chk] = lst[chk], lst[chk - 1] ###최적화인 이유
            chk -= 1                                        ##오른쪽 while문 때문에 도중에 왼쪽이 정렬이 더작으면
                                                            ##멈춘다. 그래도 되는이유 앞에서 부터 i 까지는 계속
                                                            ###정렬되어왔기 때문.


### 추가 최적화  ##최초로 작은값을 만났을때 추가된 값을 넣기.
###### 1차 최적화랑 비교해서 메모리는 같고 실행시간 은 줄었따
######일반 삽입정렬이랑 비교하면 실행시간은 비슷하고 메모리가 줄었다. 제일 좋은듯
def selectSort3(lst):
    for end in range(1, len(lst)):  ##1 2 3 4 5
        nowNum = lst[end]
        chk = end
        while chk > 0 and lst[chk-1] > nowNum:  ###가다가 도중에 왼쪽이 더 작을때까지 돌아감
            lst[chk] = lst[chk-1]          ##값을 한칸씩 오른쪽으로 insert. (원래값은 nowNum)에 남아있음
            chk -= 1
        ###while문이 끝난 것은 왼쪽값이 nowNum 보다 작다는 것이고
        lst[chk] = nowNum  ##거기에 nowNum을 넣어준다.


testNum = int(input())

for test in range(1, testNum+1):
    N = int(input())  #리스트 길이
    lst = list(map(int, input().split()))  #숫자리스트 str값으로 받음
    selectSort(lst)

    print(f"#{test} {' '.join(map(str,lst))}")

    ##삽입 정렬
