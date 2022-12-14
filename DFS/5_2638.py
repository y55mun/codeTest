import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

def check(cheese, n, m):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                return False
    return True

def dfs(cheese, n, m, i, j):
    for k in range(4):
        x,y = i+dx[k], j+dy[k]
        if 0<=x<n and 0<=y<m and not visit[x][y]:
            if cheese[x][y] != 0:
                cheese[x][y] += 1
            else:
                visit[x][y] = 1
                dfs(cheese, n, m, x, y)

def remove_cheese(cheese, n, m):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
            elif cheese[i][j] > 0:
                cheese[i][j] = 1
    return cheese

res = 0
while True:
    if check(cheese, n, m):
        print(res)
        break
        visit = [[0 for _ in range(m)] for _ in range(n)]

        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        visit[0][0] = 1
        dfs(cheese, n, m, 0,0)
        cheese = remove_cheese(cheese, n, m)
        res += 1