lst = list(map(int,input().split()))

if lst[0] - lst[1] == -1:
    chk = 1
elif lst[0] - lst[1] == 1:
    chk = -1
else:
    chk = 0

for i in range(1,len(lst)-1):
    if chk == 1:
        if lst[i] - lst[i+1] == -1:
            continue
        chk = 0
        break
    elif chk == -1:
         if lst[i] - lst[i+1] == 1:
            continue
         chk =0
         break


if chk == 1:
    print('ascending')
elif chk ==0:
    print('mixed')
else:
    print('descending')

