""" 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""

"""
- 아이디어


"""
from collections import deque

def solution(graph):
    def bfs(y, x):
        # 큐 생성 후 초기값 추가
        q = deque()
        q.append((y, x))

        while q:
            # x,y 좌표 받기
            y, x = q.popleft()

            # 상하좌우로 탐색
            dy = [0, 1, 0, -1]
            dx = [1, 0, -1, 0]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위를 벗어나는 경우 무시시
               if nx < 0 or ny < 0 or nx >= len(graph[0]) or ny >= len(graph):
                    continue

                # 벽인 경우 무시
               if graph[y][x] == 0:
                    continue

                # 방문하지 않았을 경우
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1     # 이전 좌표값 +1

                    q.append((ny, nx))  # 큐에 새로 추가

        # 상대 진영에 방문한 적이 없다면
        if graph[len(graph) - 1][len(graph[0]) - 1] == 1:
            return -1

        # 상대 진영에 방문한 적이 있다면 기록 반환
        else:
            return graph[len(graph) - 1][len(graph[0]) - 1]

    answer = bfs(0, 0)
    return answer