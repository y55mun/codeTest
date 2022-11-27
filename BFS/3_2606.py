""" 백준 2606 - 바이러스
1. 아이디어
- 값 1 && 방문 X => BFS
- BFS 돌면서 갯수 구하기

2. 시간복잡도
O(V+E)

3. 자료구조
- 전체: computers[][]
- 값 확인: visited[][]

"""

from collections import deque

import sys

n = int(input())
m = int(input())

computers = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    x,y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)

def bfs(computers, v):
    global cnt
    q = deque([v])

    while q:
        pop = q.popleft()
        visited[pop] = True

        for i in computers[pop]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                cnt += 1
    print(cnt)



bfs(computers,1)