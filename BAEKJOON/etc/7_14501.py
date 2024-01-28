""" 퇴사
https://www.acmicpc.net/problem/14501

d[i]: i번째 ~ 퇴사일 까지 벌 수 있는 최대 수입
"""
# 백트래킹
def dfs(n, sm):
    global ans

    # 1) 종료 조건: 가능한 n을 종료에 관련된 것으로 정의
    if n >= N:
        ans = max(ans, sm)
        return

    # 2) 하부 호출: 화살표 개수 만큼 호출
    if n+T[n] <= N: # 상담 하는 경우 (퇴사일 전 완료 가능할 때만 상담)
        dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)    # 상담 하지 않은 경우 (항상 가능)

N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)




## DP
import sys
input = sys.stdin.readline

n = int(input())
d = [0]*(n+2)   # 오늘 ~ 퇴사일까지 벌 수 있는 최대 수입
t = [0]*(n+1)   # 상담에 필요한 일수
p = [0]*(n+1)   # 상담 완료 시 수입

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i+t[i] > n+1:    # i번째 상담을 퇴사일까지 끝낼 수 없을 때
        d[i] = d[i+1]

    else:   # i번째 상담을 퇴사일까지 끝낼 수 있을 때
        d[i] = max(d[i+1], p[i]+d[i+t[i]])

print(d[1])
