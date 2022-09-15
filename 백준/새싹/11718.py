import sys
sys.stdin = open('11718.txt')
while 1:
    try:
        print(input())
    except EOFError:
        break

