""" 마법사 상어와 비바라기
풀이날짜: 23-11-03
https://www.acmicpc.net/problem/21610

참고: https://velog.io/@7h13200/Python%EB%B0%B1%EC%A4%80-21610%EB%B2%88-%EB%A7%88%EB%B2%95%EC%82%AC-%EC%83%81%EC%96%B4%EC%99%80-%EB%B9%84%EB%B0%94%EB%9D%BC%EA%B8%B0
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(n)]
move_order = [list(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
cloud = [[n-1,0], [n-1, 1], [n-2, 0], [n-2, 1]]

# 모든 명령에 대해서
for dir, speed in move_order:
    # 모든 구름들이
    for i in range(len(cloud)):
        # 위치를 옮김
        x = cloud[i][0] + (speed*dx[dir-1])
        y = cloud[i][1] + (speed*dy[dir-1])

        # 영역을 벗어났을때 다시 이어지므로 나머지 처리
        x %= n
        y %= n

        # 비가 오니까 물 추가
        map_list[x][y] += 1
        cloud[i] = [x,y]

    for x,y in cloud:

        # 대각선 방향으로 물복사 버그
        for dir_ in range(1, 8, 2):
            nx = x + dx[dir_]
            ny = y + dy[dir_]

            if 0<=nx<n and 0<=ny<n:
                # 구름이 사라진 칸인지 체크하기 위해 음수 처리 하므로
                # 음수인 경우에도 물이 있는 경우임!
                if map_list[nx][ny] != 0:
                    map_list[x][y] += 1

        # 구름을 생성할때 구름이 사라진 칸인지 체크하기 위한 음수 처리
        map_list[x][y] *= -1

    # 구름이 모두 사라진다.
    cloud.clear()

    # 모든 바구니를 돌며 구름 생성
    # 이때 구름이 사라진건 음수 이므로 구름이 생성되지 않고
    # 음수인 칸은 다시 양수로 바꿔줌!!
    for i in range(n):
        for j in range(n):
            if map_list[i][j] >= 2:
                cloud.append([i, j])
                map_list[i][j] -= 2

            elif map_list[i][j] < 0:
                map_list[i][j] *= -1

ans = 0
for i in range(n):
    for j in range(n):
        ans += map_list[i][j]

print(ans)