def BubbleSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[i]

    # O(n2)  최악 수행시간 O(n2)  비교와 교환.  코딩이 가장 손쉽다.