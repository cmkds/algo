a = list(input())
# print(a)
# print(len(a)//2)
# print(a[:3])
##문자열이라 슬라이싱 안됨 for문으로 합구하기
# b =sum(a[:len(a)//2])
# c=sum(a[len(a)//2 : len(a)])

left = 0
right = 0
for i in range(len(a)//2):
    left += int(a[i])
for i in range(len(a)//2,len(a)):
    right += int(a[i])
# print(left, right)
if left == right:
    print('LUCKY')
else:
    print('READY')