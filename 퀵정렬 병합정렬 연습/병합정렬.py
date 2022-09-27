def merge_sort(lst):
    if len(lst) == 1:   ##길이가 1. 더이상 자를 게 없으면
                        ##리턴
        return lst
    middle = len(lst)//2 ##리스트 길이의 절반은 middle로
                         ##잡아 준다.
    left = lst[:middle]  ##미들을 기준으로 왼쪽 자르기
    right = lst[middle:] ##미들을 기준으로 오른쪽 자르기

    left = merge_sort(left) ##왼쪽자른 것을 다시 자르고 왼쪽에 넣어준다
    right = merge_sort(right) ##오른쪽 자른 것을 또 자르고 오른쪽에 넣어준다.

    return
