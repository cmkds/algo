import sys
sys.stdin = open('baek1991.txt')

def pre(n):
    global sPre
    if n:
        sPre += chr(n+64)
        pre(ch1[n])
        pre(ch2[n])

def inorder(n):
    global sIn
    if n:
        inorder(ch1[n])
        sIn += chr(n+64)
        inorder(ch2[n])

def post(n):
    global sPost
    if n:
        post(ch1[n])
        post(ch2[n])
        sPost += chr(n+64)


N = int(input())

lst = list(input().split() for _ in range(N))

ch1 = [0]*(N+1)
ch2 = [0]*(N+1)

# print(lst)
for l in lst:
    idx = ord(l[0])-ord('@')
    if l[1].isalpha():
        ch1[idx] = ord(l[1])-ord('@')
    if l[2].isalpha():
        ch2[idx] = ord(l[2])-ord('@')

# print(ch1)
# print(ch2)
sPre =''
sIn =''
sPost =''
pre(1)
inorder(1)
post(1)

print(sPre)
print(sIn)
print(sPost)