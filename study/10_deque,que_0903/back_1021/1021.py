import sys

sys.stdin = open('input.txt')

from collections import deque

dq =deque()

N, M = map(int,input().split()) ##큐의 크기, 뽑아내려고 하는수.