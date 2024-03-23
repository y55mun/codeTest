""" [PCCP 모의고사 #2] 4번 - 보물 지도
https://school.programmers.co.kr/learn/courses/15009/lessons/121690
"""
from collections import deque

def solution(n, m, hole):
    ans = 0     # 현재까지 이동한 거리

    # 이동할 4가지 방향
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    board = [[0] * m for _ in range(n)]  # m개 짜리가 n개 생김

    for a, b in hole:
        board[a - 1][b - 1] = 1

    q = deque()
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][False] = True     # 신발을 사용하지 않고 (0,0) 방문
    q.append((0, 0, False))

    while q:
        for _ in range(len(q)): # 같은 거리에 있는 모든 위치를 동시에 처리하기 위해 사용
            ex, ey, used = q.popleft()
            for k in range(4):
                nx = ex + dx[k]
                ny = ey + dy[k]

                # 1: 함정이 없는 위치로 이동이 가능한 경우
                # 새 위치가 보드 내에 있고, 아직 지나가지 않았고, 함정이 아니라면 큐에 다음 자리 추가
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and board[nx][ny] == 0:
                    if (nx, ny) == (n - 1, m - 1):  # 현재 탐색중인 위치가 목표 위치인 경우
                        return ans + 1  # 현재 거리에 1을 더함
                    visited[nx][ny][used] = True
                    q.append((nx, ny, used))

                # 2: 함정을 건너뛸 수 있는 경우
                # 아이템 사용하지 않았으므로, 현재 위치에서 같은 방향으로 2칸 이동하여 함정을 건너 뛴다.
                if not used:
                    nx += dx[k]
                    ny += dy[k]

                    # 새 위치가 보드 내에 있고, 신발을 사용한 채 지나가지 않았으며, 함정이 아니라면
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][True] and board[nx][ny] == 0:
                        if (nx, ny) == (n - 1, m - 1):
                            return ans + 1
                        visited[nx][ny][True] = True
                        q.append((nx, ny, True))
        ans += 1

    return -1
