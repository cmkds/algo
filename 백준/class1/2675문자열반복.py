testNum = int(input())

for test in range(1,1+testNum):
    a, b=map(str,input().split())
    a = int(a)
    new=''
    for i in b:
        for _ in range(a):
            new+=i
    print(new)