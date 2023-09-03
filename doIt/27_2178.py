""" 미로 탐색
https://www.acmicpc.net/problem/2178
"""
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0 , -1, 0]

def bfs(y,x):
    q = deque()
    visited[0][0] = 1
    q.append((y,x))

    while q:
        ey, ex = q.popleft()

        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0<= ny < n and 0 <= nx < m:
                if a[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[ey][ex] + 1
                    q.append((ny,nx))

    return visited[n-1][m-1]

print(bfs(0,0))
