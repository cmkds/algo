s='Reverse this strings'
##1
s = s[::-1]
print(s)
################################2
s='Reverse this strings'
lst = []
for char in s:
    lst.append(char)
lst.reverse()
s =''.join(lst)
print(s)
###############3
s='Reverse this strings'
lst = []
for char in s:
    lst.append(char)
for i in range(len(lst)//2):
    lst[i], lst[-i-1] = lst[-i-1], lst[i]
s =''.join(lst)
print(s)

######## 4
s='Reverse this strings'
ans=''
for char in s:
    ans = char + ans
print(ans)

############5
s='Reverse this strings'
ans=''
for idx in range(len(s)-1, -1, -1):
    ans += s[idx]
print(ans)