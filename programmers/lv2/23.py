""" 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""

"""
- 아이디어


"""

from collections import deque
import sys


def solution(maps):
    answer = 0

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    def bfs(y, x):
        q = deque()
        q.append((y, x))

        while q:
            ey, ex = q.popleft()

            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]

                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue

                # 벽이면 무시
                if maps[ny][nx] == 0: continue

                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[ey][ex] + 1
                    q.append((ny, nx))

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = bfs(0, 0)

    return -1 if answer == 1 else answer