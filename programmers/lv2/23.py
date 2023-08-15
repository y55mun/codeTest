""" 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""

"""
- 아이디어


"""
from collections import deque

def solution(graph):
    # BFS 함수
    def bfs(y, x):

        q = deque()
        q.append((y, x))

        while q:
            y, x = q.popleft()

            dy = [0, 1, 0, -1]
            dx = [1, 0, -1, 0]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= len(graph[0]) or ny >= len(graph):
                    continue

                if graph[y][x] == 0:
                    continue

                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1

                    q.append((ny, nx))

        if graph[len(graph) - 1][len(graph[0]) - 1] == 1:
            return -1


        else:
            return graph[len(graph) - 1][len(graph[0]) - 1]

    answer = bfs(0, 0)
    return answer