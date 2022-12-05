from collections import deque

def BFS(y,x):
    q.append((y,x))
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    visited[y][x] = 1

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<= nx < N and 0<=ny<N and a[ny][nx] == a[y][x] and not visited[ny][nx]:
                visited[ny][nx] = 1  # 방문체크 후 큐에 넣음
                q.append((ny,nx))


N = int(input())
a = [list(input()) for _ in range(N)]
q = deque()

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for j in range(N):
    for i in range(N):
        if not visited[j][i]:  # 아직 방문 안한 경우만 체킹
            BFS(j, i)
            cnt1 += 1

# 적록색약인 경우
for j in range(N):
    for i in range(N):
        if a[j][i] == 'G':
            a[j][i] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for j in range(N):
    for i in range(N):
        if not visited[j][i]:
            BFS(j, i)
            cnt2 += 1

print(cnt1, cnt2)