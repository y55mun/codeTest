""" 벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
"""

from collections import deque

def bfs():
    q = deque()
    q.append([0,0,0])

    while q:
        cur_r, cur_c, breakable = q.popleft()

        if cur_r == row_len - 1 and cur_c == col_len - 1:
            return visited[cur_r][cur_c][breakable]

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc

            if next_r <= -1 or next_r >= row_len or next_c <= -1 or next_c >= col_len:
                continue

            # 다음 이동할 곳이 벽이고 벽 파괴 기회를 사용하지 않은 경우 -> 벽 부수기
            if grid[next_r][next_c] == 1 and breakable == 0:
                visited[next_r][next_c][1] = visited[cur_r][cur_c][0] + 1
                q.append([next_r, next_c, 1])

            # 다음 이동할 곳이 벽이 아니고 한번도 방문하지 않음
            elif grid[next_r][next_c] == 0 and visited[next_r][next_c][breakable] == 0:
                visited[next_r][next_c][breakable] = visited[cur_r][cur_c][breakable] + 1
                q.append([next_r, next_c, breakable])

    return -1


row_len, col_len = map(int, input().split())
grid = [list(map(int, input())) for _ in range(row_len)]

visited = [[[0,0] for _ in range(col_len)] for _ in range(row_len)]     # 이건 됨
visited[0][0][0] = 1

directions = [(1,0), (-1,0), (0,1), (0,-1)]

print(bfs())