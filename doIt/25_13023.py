"""ABCDE
https://www.acmicpc.net/problem/13023

1. 아이디어
- 노드에 연결되어 있는 값들을 넣고 조건 확인
-
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arrive = False
a = [[] for _ in range(n+1) ]
visited = [[False]*(n+1)]

def dfs(now,depth):
    if depth == 5:
        arrive = True
        return
    visited[now] = True