import sys
input = sys.stdin.readline

def push(X,lst):
    lst.append(X)

def pop(lst):
    if lst:
        return lst.pop()
    else:
        return '-1'
def size(lst):
    return len(lst)

def empty(lst):
    if lst:
        return '0'
    else:
        return '1'
def top(lst):
    if lst:
        return lst[-1]
    else:
        return '-1'

n = int(input())
lst = []
for i in range(n):
    a = input().split()
    if a[0] =='push':
        push(a[1],lst)

    elif a[0] == 'top':
        print(top(lst))
    elif a[0] == 'size':
        print(size(lst))
    elif a[0] == 'pop':
        print(pop(lst))
    elif a[0] =='empty':
        print(empty(lst))
    # print(a,lst)
    # print('####')
