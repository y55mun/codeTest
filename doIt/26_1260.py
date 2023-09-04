""" DFS와 BFS
https://www.acmicpc.net/problem/1260

"""
from collections import deque

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, start = map(int, input().split())
a = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

# 방문할 수 있는 노드가 여러개일 경우 번호가 작은 것을 먼저 방문하기 위해 정렬
for i in range(n+1):
    a[i].sort()

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            dfs(i)
visited = [False] * (n+1)
dfs(start)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in a[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (n+1)
bfs(start)

