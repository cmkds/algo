def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2

    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    res = []
    i,j = 0,0
    if left[-1] > right[-1]:
        cnt += 1

    while i <len(left) or j < len(right):

        if i <len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        elif i <len(left):
            res.append(left[i])
            i += 1
        elif j < len(right):
            res.append(right[j])
            j+= 1
    return res



testNum = int(input())
for test in range(1,1+testNum):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    res = merge_sort(lst)
    print(f'#{test} {res[N//2]} {cnt}')