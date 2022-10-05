n = int(input())

for i in range(n):
    a = input()
    stack = 0
    for i in a:
        if i =="(":
            stack +=1
        else:
            if stack <=0:
                print('NO')
                break
            else:
                stack -=1
    else:
        if stack ==0:
            print('YES')
        else:
            print('NO')