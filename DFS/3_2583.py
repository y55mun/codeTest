""" 백준 2583



"""


import sys

sys.setrecursionlimit(10000)


def dfs(y, x, cnt):
    graph[y][x] = 1

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<M and 0<=nx<N:
            if graph[ny][nx] == 0:
                cnt = dfs(ny, nx, cnt+1)
    return cnt



M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
dy = [0,1,0,-1]
dx = [1,0,-1,0]

res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            res.append(dfs(i,j,1))
print(len(res))
print(*sorted(res))
