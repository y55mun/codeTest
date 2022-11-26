""" 백준 2667: 단지번호붙이기
1. 아이디어
- 방문 여부(chk), 길이 맞는지(map 값이 1인지)
- BFS 돌면서 총 갯수 + 1, 각각 값 저장

2. 시간복잡도
- O(V+E)
- V: 25*25
- E: 4*25*25

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문 여부: bool[][]
"""

from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().rstrip())) for _ in range(n)]
chk = [[False]*n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y,x):
    rs = 1

    q = deque()
    q.append((y,x))

    while q:
        ey, ex = q.popleft()

        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0<= ny < n and 0<= nx < n:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))

    return rs

cnt = 0
ans = []

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            ans.append(bfs(j, i))
ans.sort()

print(cnt)
for k in ans:
    print(k)