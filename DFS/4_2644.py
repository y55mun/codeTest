import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

result = []
cnt = 0


def dfs(graph, v, visited):
    global cnt
    cnt += 1
    visited[v] = True

    if v == b:
        result.append(cnt)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, a, visited)

