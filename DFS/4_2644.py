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

# A부터 시작하여 B까지 도달하는 거리가 촌수
def dfs(graph, v, visited):
    global cnt
    cnt += 1    # DFS를 재귀적으로 구연하여 재귀 깊이가 깊어질 때 num의 값을 +1
    visited[v] = True

    if v == b:
        result.append(cnt)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, a, visited)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)