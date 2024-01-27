""" 퇴사
https://www.acmicpc.net/problem/14501

d[i]: i번째 ~ 퇴사일 까지 벌 수 있는 최대 수입
"""

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
