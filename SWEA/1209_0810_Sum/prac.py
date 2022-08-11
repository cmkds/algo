#리스트를 세로로 쌈빡하게 묶는 방법
lst = [[1,2,3],[4,5,6],[7,8,9]]
   # print(*i)
print()
##########zip이랑 애스더 리스크를 쓰면 리스트를 막 돌릴 수 있다.

#1
lst =list(zip(*lst))
#2
lst2 = list(map(list,zip(*lst)))
print(lst)
for i in lst:
    print(*i)

########

lst2 = list(zip(*lst))[::-1]
for i in lst2:
    print(*i)


lst3 = list(zip(*lst[::-1]))
for i in lst3:
    print(*i)