def f(i,r):
    if i ==r:
        lst.append(bit[:])
        return
    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            f(i+1,r)

N = 4
bit = [0] * N
lst = []
f(0,4)
print(lst)