"""
https://www.acmicpc.net/problem/3187
"""

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
garden = [list(input()) for _ in range(r)]

k, v = 0, 0 # 늑대, 양

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    a, b = 0, 0
    q = [(y, x)]

    while q:
        y, x = q.pop()

        if garden[y][x] == "v":
            b += 1

        if garden[y][x] == "k":
            a += 1

        garden[y][x] = "#"

        # 4방향 회전으로 탐색
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0<= ny < r and 0<=nx < c:
                if garden[ny][nx] != "#":
                    q.append((ny, nx))

    if a <= b:
        a = 0
    else:
        b = 0
    return a,b


for j in range(r):  # 세로
    for i in range(c):  # 가로
        if garden[j][i] == "v" or garden[j][i] == "k":
            a, b = bfs(j, i)
            k += a
            v += b

print(k, v)