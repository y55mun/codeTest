"""ABCDE
https://www.acmicpc.net/problem/13023

"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
arrive = False
a = [[] for _ in range(n+1)]
visited = [[False]*(n+1)]

def dfs(now,depth):
    global arrive
    if depth == 5:
        arrive = True
        return

    # 방문 리스트에 현재 노드 방문 기록 저장
    visited[now] = True

    # 방문 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행
    for i in a[now]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[now] = False

for _ in range(m):
    s,e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n):
    # 노드마다 dfs 실행
    dfs(i,1)

    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)