a,b = map(int,input().split())
c= int(input())


k, b =divmod(b+c, 60)
a += k

print(a%24,b)
