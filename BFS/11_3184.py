'''
입력:
8 8
.######.
#..o...#
#.####.#
#.#v.#.#
#.#.o#o#
#o.##..#
#.v..v.#
.######.

출력:
3 1

'''

# BFS 이동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(x, y):
    queue = [(x, y)]
    o, v = 0, 0
    while queue:
        x, y = queue.pop()

        # 늑대일 경우 w에 1 추가
        if board[x][y] == 'v':
            v += 1

        # 양 일 경우 o에 1 추가
        if board[x][y] == 'o':
            o += 1

        board[x][y] = '#'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 마당 범위 안에 있고, 방문하지 않았고, #이 아니면 BFS
            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] != '#':
                    queue.append((nx, ny))
    if o <= v:
        o = 0
    else:
        v = 0
    return o, v


M, N = map(int, input().split())
board = [list(input()) for _ in range(M)]
O, V = 0, 0     # O: 양, V: 늑대
for i in range(M):
    for j in range(N):
        if board[i][j] == 'v' or board[i][j] == 'o':
            o, v = bfs(i, j)
            O += o
            V += v

print(O, V)     # 양, 늑대 출력
