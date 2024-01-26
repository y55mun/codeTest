import sys

input = sys.stdin.readline

n = int(input())
d = [0] * (n + 2)   # i번째 ~ 퇴사날까지 받을 수 있는 최대 이익
t = [0] * (n + 1)
p = [0] * (n + 1)

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i + t[i] > n + 1:    # 상담에 필요한 일수가 퇴사일 넘길때
        d[i] = d[i + 1] # 다음날 값 그대로 가져옴
    else:
        d[i] = max(d[i + 1], p[i] + d[i + t[i]])     #오늘 상담을 안 할 경우와 상담을 할 경우 중 max 값

print(d[1])