a = input().lower()

x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
y=[0]*26

for m in a:
    for i in range(26):
        if x[i] == m:
            y[i] += 1

z = max(y)
idx = y.index(z)
chk = 0
for a in y:
    if a==z:
        chk +=1
if chk ==1:
    print(x[idx].upper())
else:
    print('?')
