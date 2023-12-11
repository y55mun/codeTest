""" 숨바꼭질 3
https://www.acmicpc.net/problem/13549
"""

import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
limit = 100001
time = [0] * limit


def bfs(x, y):
    q = deque()
    if x == 0:
        q.append(1)
    else:
        q.append(x)

    while q:
        x = q.popleft()
        if y == x:
            return time[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < limit and time[nx] == 0:   # 범위 내에 있고 탐색하지 않았을 때
                if nx == 2 * x:     # 2*x 먼저 탐색해야 하니 큐의 맨 앞에 넣어줌
                    time[nx] = time[x]
                    q.appendleft(nx)
                else:       # 그렇지 않으면 이전 시간 + 1
                    time[nx] = time[x] + 1
                    q.append(nx)


# 엣지 케이스 - if 문으로 따로 처리하는게 이득임
if a == 0:
    print(bfs(a, b) + 1)
else:
    print(bfs(a, b))