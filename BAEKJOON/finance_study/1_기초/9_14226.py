""" 이모티콘
https://www.acmicpc.net/problem/14226
"""
from collections import deque

n = int(input())  # 이모티콘 갯수
dist = [[-1] * (n + 1) for _ in range(n + 1)]

q = deque()
q.append((1, 0))    # 화면 이모티콘 개수(현재 이모티콘 개수), 클립보드 이모티콘 개수
dist[1][0] = 0

while q:
    s, c = q.popleft()

    if dist[s][s] == -1:    # 방문하지 않았으면
        dist[s][s] = dist[s][c] + 1     # 화면에 있는 이모티콘을 복사해서 클립보드에 저장
        q.append((s, s))
    if s + c <= n and dist[s + c][c] == -1:     # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
        q.append((s + c, c))
    if s - 1 >= 0 and dist[s - 1][c] == -1: # 화면에 있는 이모티콘 중 하나 삭제
        dist[s - 1][c] = dist[s][c] + 1
        q.append((s - 1, c))

ans = -1
for i in range(n + 1):
    if dist[n][i] != -1:
        if ans == -1 or ans > dist[n][i]:
            ans = dist[n][i]

print(ans)