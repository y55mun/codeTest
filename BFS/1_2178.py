""" 백준 2178
1. 아이디어
- 방문 X && 길이 맞음 -> BFS

2. 시간 복잡도
- O(V+E)
- V: 100*100
- E: 4*100*100
- V+E: 5000000=500만

3. 자료구조
- 방문 여부: chk[][]
  길이 맞는지 확인: map[][]
"""

from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

"""
<input>
101111
101010
101011
111011

<output>
[[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

"""
map = [list(map(int, input().strip())) for _ in range(n)]

# 방문 했는지 확인
chk = [[False] * m for _ in range(n)]

# 이동할 4가지 방향
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q=deque()
    chk[0][0] = 1   # 출발
    q.append((y, x))

    while q:
        ey, ex = q.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0<= ny <n and 0<= nx <m:
                if map[ny][nx] == 1 and chk[ny][nx] == 0:   # 길이 있고, 아직 방문 안했으면
                    chk[ny][nx] = chk[ey][ex] + 1   # 몇 번째 방문인지 현재 좌표의 방문 값에 1을 더해줌
                    q.append((ny, nx))

    return chk[n-1][m-1]    # 방문 배열의 가장 마지막 요소를 출력하면 몇 번째 만에 도착인지 알 수 있다.

print(bfs(0,0)) # 첫 번째 위치가 문제에 주어져 있음