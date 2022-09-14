lst =[]
for i in range(9):
    lst.append(int(input()))
a=max(lst)
print(a)
idx = lst.index(a)
print(idx+1)