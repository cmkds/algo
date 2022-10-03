N,K = map(int,input().split())

a=1
b=1

for i in range(N,N-K,-1):
    # print(i)
    a *= i
for i in range(1,K+1):
    # print(i)
    b *= i
print(a//b)