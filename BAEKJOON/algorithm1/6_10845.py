""" 큐
https://www.acmicpc.net/problem/10845
"""
import sys
from collections import deque

input = sys.stdin.readline  # readline 뒤에 () 붙이니 에러 났었음

dq = deque()

n = int(input())

for i in range(n):
    command = input().split()

    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        if len(dq) != 0:
            dq.popleft()
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)