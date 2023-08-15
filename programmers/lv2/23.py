""" 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""

"""
- 아이디어


"""
from collections import deque


def solution(graph):
    # 행,열 길이 정리
    row = len(graph)
    col = len(graph[0])

    # BFS 함수
    def bfs(y, x):
        # 큐 생성 후 초기값 추가
        q = deque()
        q.append((y, x))

        while q:
            # ex(행),ey(열) 좌표 받기
            ey, ex = q.popleft()

            # 방향 벡터(상,하,좌,우)로 탐색
            dy = [0, 1, 0, -1]
            dx = [1, 0, -1, 0]

            for i in range(4):
                nx = ex + dx[i]
                ny = ey + dy[i]
                # 범위를 벗어나는 경우 무시
                if nx < 0 or ny < 0 or nx >= len(graph[0]) or ny >= len(graph):
                    continue
                # 벽인 경우 무시
                if graph[ey][ex] == 0:
                    continue
                # 방문한 적이 없는 경우에만
                if graph[ny][nx] == 1:
                    # 이전 좌표값 +1
                    graph[ny][nx] = graph[ey][ex] + 1

                    # 큐에 새로 추가
                    q.append((ny, nx))

        # 상대 진영에 방문한 적이 없다면
        if graph[len(graph) - 1][len(graph[0]) - 1] == 1:
            return -1

        # 상대 진영에 방문했다면 기록 반환
        else:
            return graph[len(graph) - 1][len(graph[0]) - 1]

    answer = bfs(0, 0)
    return answer