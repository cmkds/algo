가로행을 더하는 변수와 세로행을 더하는 변수를 만들어서하면

for문을 2번쓸 필요 없이
한번 돌릴 때 두가지 둘다 구할 수
if 있다:

    i 포문
        j 포문
            tmp_sum_row += lst[i][j]
            tmp_sum_col += lst[j][i]
    tmp = 0
    #대각선
    for i in range(n):
        tmp += lst[i][j]
        tmp_reverse = lst[-i][-j-1]
 #인데 여기서 대각선의 i for문과 i의 포문을 합칠수가 있어서
 #더 줄일 수 있다.


 ## 가로행 더하기

    sum_lst = max(list(map(sum, lst))) #이게 가로라인들의 최대값을 구하는 함수
                            #세로는 이 방법으로 못한다.
    lst_trans = zip(*lst)
    sum_lst_trans = max(list(map(sum, lst_trans)))
    #우하향 대각선 리스트 만들기.
    [lst[i][i] for i in range(n)]

    sum_dia = sum([lst[i][i] for i in range(n)])
    sum_dia_reverse = sum([lst[-i][-i-1] for i in range(n)])