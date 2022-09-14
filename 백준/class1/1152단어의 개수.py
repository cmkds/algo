a = input().strip()

cnt =1
for i in a:
    if i ==' ':
        cnt+=1
if a=='':
    print(0)
else:
    print(cnt)