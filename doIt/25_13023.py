"""ABCDE
https://www.acmicpc.net/problem/13023
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
arrive = False
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

def dfs(now, depth):
    global arrive
    visited[now] = True
    if depth == 5:
        arrive = True
        return

    for i in a[now]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[now] = False



for i in range(n):
    dfs(i, 1)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)