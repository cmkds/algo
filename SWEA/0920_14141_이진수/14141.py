import sys
sys.stdin = open('input.txt')

dic ={
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15,
}

testNum = int(input())

for test in range(1,1+testNum):
    n, s = input().split()
    for i in s:
        try:
            a = int(i)
            print(bin(a))
        except:
            a = dic.get(i)
            print(bin(a))
