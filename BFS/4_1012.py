""" 백준 1012- 유기농 배추
1. 아이디어


2. 시간복잡도


3. 자료구조


"""
import sys
from collections import deque

read = sys.stdin.readline

# 이동할 4가지 방향
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]



def bfs(y,x):
    q = deque()
    q.append((y, x))

    while q:
        ey, ex = q.popleft()

        for k in range(4):
            ny = ey + dy[k]
            nx = ey + dx[k]

            if 0 <= ny <n and 0 <= nx < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((ny, nx))

t = int(read())    # 테스트 케이스
cnt = 0

for _ in range(t):
    m, n, k = map(int, read().split())
    graph = [[0]*m for _ in range(n)]
    #chk = [[False] * m for _ in range(n)]
    #cnt = 0

    for _ in range(k):
        x,y = map(int, read().split())
        graph[y][x] = 1

    cnt = 0
    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1:
                #chk[j][i] = True
                #graph[j][i] = 0
                bfs(j,i)
                cnt += 1
    print(cnt)