"""
1. 자료구조


1. 같은 울타리 영역 안에서 검사
양(k) > 늑대(v): 늑대 전부 out

정답: 양 늑대
"""
from collections import deque

import sys
input = sys.stdin.readline

r, c = map(int, input().split())    # 세로, 가로
board = [list(input()) for _ in range(r)]
K, V = 0, 0    # 양, 늑대


def bfs (x, y):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    q = [(x,y)]
    k, v = 0, 0

    while q:
        x, y = q.pop()

        # 늑대 일 경우 늑대 추가
        if board[x][y] == "v":
            v += 1

        if board[x][y] == "k":
            k += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx < c and 0<= ny < r:
                if board[nx][ny] != "#":
                    q.append((nx, ny))


for j in range(r):
    for i in range(c):
        if board[j][i] == "k" and board[j][i] == "v":
            k, v = bfs(k, v)
            K += k
            V += v

# print(k,v)