n = int(input())
lst = []
for _ in range(51):
    lst.append([])
for _ in range(n):
    s = input()
    if s not in lst[len(s)]:
        lst[len(s)].append(s)

# print(lst)
for i in range(1,51):
    set(lst[i])
    lst[i].sort()

# print(lst)
for i in range(1,51):
    for j in range(len(lst[i])):
        if lst[i][j]:
            print(lst[i][j])