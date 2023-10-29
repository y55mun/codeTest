"""

양 > 늑대: 늑대 --
이 외는 양--
"""
from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(x,y):
    q = deque()
    q.append((y,x))

    k,v = 0, 0

    while q:
        x, y = q.pop()

        if garden[x][y] == "v":
            v+=1



r, c = map(int, input().split())
garden = [list(input().split()) for _ in range(c)]
visited = [[0]*r for _ in range(c)] # 방문 여부
sheepCount, wolvesCount = 0,0

for j in range(r):  # 세로
    for i in range(c):  # 가로
        if garden[j][i] == 'k' and garden[j][i] == 'v'
            k, v = bfs(k,v)
            sheepCount += k
            wolvesCount += v
print(sheepCount,wolvesCount)

