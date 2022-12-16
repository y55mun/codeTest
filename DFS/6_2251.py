import sys


def dfs(a, b, c, visit):
    # 물통 A가 빈 경우, 물통 C 용량의 경우의 수를 카운팅
    if a == 0:
        ans[c] += 1

    # 물통 A에서 옮기는 경우
    if a > 0:
        # 물통 B로 옮길 수 있는 경우
        if b < B:
            # 물통 B의 남은 용량
            l = B - b
            # B가 가득찰 때까지 붓는다
            if a >= l:
                if not visit[a - l][B][c]:
                    visit[a - l][B][c] = 1
                    dfs(a - l, B, c, visit)
                    visit[a - l][B][c] = 0
            # A가 빌 때까지 붓는다
            elif not visit[0][b + a][c]:
                visit[0][b + a][c] = 1
                dfs(0, b + a, c, visit)
                visit[0][b + a][c] = 0

        # 물통 C로 옮길 수 있는 경우
        if c < C:
            # 물통 C의 남은 용량
            l = C - c
            # C가 가득찰 때까지 붓는다
            if a >= l:
                if not visit[a - l][b][C]:
                    visit[a - l][b][C] = 1
                    dfs(a - l, b, C, visit)
                    visit[a - l][b][C] = 0
            # A가 빌 때까지 붓는다
            elif not visit[0][b][c + a]:
                visit[0][b][c + a] = 1
                dfs(0, b, c + a, visit)
                visit[0][b][c + a] = 0

    # 물통 B에서 옮기는 경우
    if b > 0:
        # 물통 A로 옮길 수 있는 경우
        if a < A:
            # 물통 A의 남은 용량
            l = A - a
            # A가 가득찰 때까지 붓는다
            if b >= l:
                if not visit[A][b - l][c]:
                    visit[A][b - l][c] = 1
                    dfs(A, b - l, c, visit)
                    visit[A][b - l][c] = 0
            # B가 빌 때까지 붓는다
            elif not visit[a + b][0][c]:
                visit[a + b][0][c] = 1
                dfs(a + b, 0, c, visit)
                visit[a + b][0][c] = 0

        # 물통 C로 옮길 수 있는 경우
        if c < C:
            # 물통 C의 남은 용량
            l = C - c
            # C가 가득찰 때까지 붓는다
            if b >= l:
                if not visit[a][b - l][C]:
                    visit[a][b - l][C] = 1
                    dfs(a, b - l, C, visit)
                    visit[a][b - l][C] = 0
            # B가 빌 때까지 붓는다
            elif not visit[a][0][c + b]:
                visit[a][0][c + b] = 1
                dfs(a, 0, c + b, visit)
                visit[a][0][c + b] = 0

    # 물통 C에서 옮기는 경우
    if c > 0:
        # 물통 A로 옮길 수 있는 경우
        if a < A:
            # 물통 A의 남은 용량
            l = A - a
            # A가 가득찰 때까지 붓는다
            if c >= l:
                if not visit[A][b][c - l]:
                    visit[A][b][c - l] = 1
                    dfs(A, b, c - l, visit)
                    visit[A][b][c - l] = 0
            # C가 빌 때까지 붓는다
            elif not visit[a + c][b][0]:
                visit[a + c][b][0] = 1
                dfs(a + c, b, 0, visit)
                visit[a + c][b][0] = 0

        # 물통 B로 옮길 수 있는 경우
        if b < B:
            # 물통 B의 남은 용량
            l = B - b
            # B가 가득찰 때까지 붓는다
            if c >= l:
                if not visit[a][B][c - l]:
                    visit[a][B][c - l] = 1
                    dfs(a, B, c - l, visit)
                    visit[a][B][c - l] = 0
            # C가 빌 때까지 붓는다
            elif not visit[a][b + c][0]:
                visit[a][b + c][0] = 1
                dfs(a, b + c, 0, visit)
                visit[a][b + c][0] = 0


A, B, C = map(int, sys.stdin.readline().split())

# 물통 C의 가능한 용량의 경우의 수를 체크 -> 0~C리터 중에서 가능
ans = [0] * (C + 1)

# 물통 A, B, C의 용량의 경우의 수를 체크 -> visit[A][B][C]
visit = [[[0] * 201 for _ in range(201)] for _ in range(201)]

# 처음에 물통 A, B는 비어있고, C는 가득차있다
dfs(0, 0, C, visit)

for i in range(C + 1):
    if ans[i] > 0: print(i, end=" ")
# 시간복잡도 = O(V+E) = O(V), 공간복잡도 = O(V)
# 최악의 경우 V = 200x200x200 = 6,000,000, E = 3x6,000,000 = 18,000,000 -> 24,000,000번의 연산 필요
# 파이썬은 2000만 번의 연산에 1초가 소요된다.