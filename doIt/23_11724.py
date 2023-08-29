"""연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in a[v]:
        if not visited[v]:
            dfs(i)

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append[e]
    a[e].append[s]

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(i)