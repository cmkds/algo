a = input()

b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c = [-1]*26

for idx,m in enumerate(a):

    k=b.index(m)
    if c[k] == -1:
        c[k]=idx

print(*c)