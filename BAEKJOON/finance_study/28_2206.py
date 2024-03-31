""" 벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
"""

from collections import deque

shortest_path_len = -1
# row_len, col_len = map(int, input().split())
# grid = [list(map(int, input())) for _ in range(row_len)]

#####테스트용
row_len, col_len = 6, 4
grid = [[0,1,0,0], [1,1,1,0], [1,0,0,0], [0,0,0,0], [0,1,1,1], [0,0,0,0]]

#####################
visited = [[False] * col_len for _ in range(row_len)]
directions = [(1,0), (-1,0), (0,1), (0,-1)]

q = deque()
q.append((0,0,1))
visited[0][0] = True

while q:
    cur_r, cur_c, cur_len = q.popleft()
    if cur_r == row_len-1 and cur_c == col_len-1:
        shortest_path_len = cur_len
        break
    for dr, dc in directions:
        next_r = cur_r + dr
        next_c = cur_c + dc

        if 0 <= next_r < row_len and 0 <= next_c < col_len:
            if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                q.append((next_r, next_c, cur_len+1))
                visited[next_r][next_c] = True
print(shortest_path_len)
