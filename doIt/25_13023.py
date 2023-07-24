"""ABCDE
https://www.acmicpc.net/problem/13023
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline()
n,m = map(int,input().split())
arrive = False
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in a[now]:
        if not visited[i]:
            dfs(now, depth+1)
    visited[now] = False
