a = input().replace(" ","")

tmp = 0
for i in a:
    tmp += (int(i))**2
print(tmp%10)