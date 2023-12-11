""" 숨바꼭질 3
https://www.acmicpc.net/problem/13549
"""

import sys
from collections import deque

def bfs():
    graph = [-1] * 100001
    graph[n] = 0
    q = deque([n])

    while q:
        target = q.popleft()

        if target == k:
            return graph[target]

        for i in (target+1, target-1, target*2):
            if 0 <= i <= 100000 and graph[i] == -1:
                if i == target*2:
                    graph[i] = graph[target]
                    q.appendleft(i)
                else:
                    graph[i] = graph[target] + 1
                    q.append(i)

n, k = map(int, sys.stdin.readline().split())
print(bfs())