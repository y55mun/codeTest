import sys

n,m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0]*m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def virus(y,x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0<=ny<m and 0<=nx<n:
            if tmp[ny][nx] == False:
                tmp[ny][nx] =2
                virus(ny,nx)


def Count():
    cnt = 0
    for j in range(m):
        for i in range(n):
            if tmp[j][i] == 0:
                cnt += 1
    return cnt


def DFS(count):
    global result
    if count == 3:
        for j in range(m):
            for i in range(n):
                tmp[j][i] = lab[j][i]
                # tmp[i].append(lab[i][j])

        for j in range(m):
            for i in range(n):
                if tmp[i][j]==2:
                    virus(j, i)
        result = max(result, Count())
        return
    else:
        for j in range(m):
            for i in range(n):
                if lab[j][i] == 0:
                    lab[j][i]=1
                    count+=1
                    DFS(count)
                    lab[j][i]=0
                    count-=1
result=0
DFS(0)
print(result)