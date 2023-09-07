""" 트리의 지름 구하기
https://www.acmicpc.net/problem/1167

"""
from collections import deque

import sys
input = sys.stdin.readline
n = int(input())
a = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        a[s].append((e,v))
        index += 2

distance = [0] * (n+1)
visited = [False] * (n+1)

