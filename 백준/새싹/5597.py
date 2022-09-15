lst = []

for i in range(1,31):
    lst.append(i)

for i in range(28):
    lst.remove(int(input()))

print(*lst, sep='\n')