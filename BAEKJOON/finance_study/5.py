""" [PCCP 모의고사 #2] 4번 - 보물 지도
https://school.programmers.co.kr/learn/courses/15009/lessons/121690
"""
from collections import deque

def solution(n, m, hole):
    ans = 0

    # 이동할 4가지 방향
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    board = [[0] * m for _ in range(n)]  # m개짜리가 n개 생김
    for a, b in hole:
        board[a - 1][b - 1] = 1

    q = deque()
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][False] = True
    q.append((0, 0, False))

    while q:
        ex, ey, used = q.popleft()

        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and board[nx][ny] == 0:
                if (nx, ny) == (n - 1, m - 1):
                    return ans + 1
                visited[nx][ny][used] = True
                q.append((nx, ny, used))
            if not used:
                nx += dx[k]
                ny += dy[k]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][True] and board[nx][ny] == 0:
                    if (nx, ny) == (n - 1, m - 1):
                        return ans + 1
                    visited[nx][ny][True] = True
                    q.append((nx, ny, True))
        ans += 1

    return -1

n = 4
m = 4
hole = [[2, 3], [3, 3]]

print(solution(n, m, hole))