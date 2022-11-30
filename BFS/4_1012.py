"""
계속 index 오류 발생했던 원인: bfs 함수에서 nx = ex + dx[k] 부분에서 ey 라고 적어서 계속 index 오류가 났다.

"""

import sys
from collections import deque

dy = [0, 1, 0, -1]  #w
dx = [1, 0, -1, 0]  #h

read = sys.stdin.readline

def bfs(y,x): # 영역 확인
    q = deque()
    q.append((y,x))
    chk[y][x] = True

    while q:
        ey, ex = q.popleft()

        for k in range(4): # 사방면 확인
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny,nx))

for _ in range(int(read())):
    m, n, k = map(int, read().split())
    graph = [[0] * m for _ in range(n)]
    chk = [[False] * m for _ in range(n)]

    result = 0

    for _ in range(k):  # 배추 위치 입력
        x, y = map(int, read().split())
        graph[y][x] = 1


    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1 and chk[j][i] == False:
                chk[j][i] = True
                result += 1
                bfs(j,i)
    print(result)