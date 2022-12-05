from collections import deque

def bfs(y,x):
    q = deque()
    q.append((y,x))

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    while q:
        ey, ex = q.popleft()

        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0<=ny<N and 0<=nx<N:
                if a[ny][nx] == a[y][x] and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append((ny, nx))



N = int(input())
a = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

# 적록색약 아닌 경우
cnt1 = 0
for j in range(N):
    for i in range(N):
        if visited[j][i] == False:
            bfs(j,i)
            cnt1 += 1

# 적록색약인 경우
for j in range(N):
    for i in range(N):
        if a[j][i] == 'G':
            a[j][i] == 'R'


visited = [[False] * N for _ in range(N)]
cnt2 = 0
for j in range(N):
    for i in range(N):
        if visited[j][i] == False:
            bfs(j,i)
            cnt2 += 1

print(cnt1, cnt2)