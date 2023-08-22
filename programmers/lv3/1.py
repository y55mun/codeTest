""" 아이템 줍기
https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102

    # 길찾기
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[0] * MAX for _ in range(MAX)]
    visited[characterX * 2][characterY * 2] = 1

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()

        if x == itemX * 2 and y == itemY*2:
            answer = (visited[x][y]-1) // 2
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if visited[nx][ny] == 0 and field[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return answer