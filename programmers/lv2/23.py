""" 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""

from collections import deque

def solution(maps):
    def bfs(y, x):
        # 큐 생성 후 초기값 추가
        q = deque()
        q.append((y, x))

        while q:
            # x(행),y(열) 좌표 받기
            ey, ex = q.popleft()

            # 방향 벡터(상,하,좌,우)로 탐색
            dy = [0, 1, 0, -1]
            dx = [1, 0, -1, 0]

            for i in range(4):
                nx = ex + dx[i]
                ny = ey + dy[i]

                # 범위를 벗어나는 경우 무시
                if nx < 0 or ny < 0 or nx >= len(maps[0]) or ny >= len(maps):
                    continue

                # 벽인 경우 무시
                if maps[ey][ex] == 0:
                    continue

                # 방문한 적이 없는 경우에만
                if maps[ny][nx] == 1:
                    # 이전 좌표값 +1
                    maps[ny][nx] = maps[ey][ex] + 1

                    # 큐에 새로 추가
                    q.append((ny, nx))

        # 상대 진영에 방문한 적이 없다면
        if maps[len(maps) - 1][len(maps[0]) - 1] == 1:
            return -1

        # 상대 진영에 방문했다면 기록 반환 (그래프의 가장 오른쪽 아래 반환)
        else:
            return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = bfs(0, 0)
    return answer