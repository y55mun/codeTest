""" 점프 점프
https://www.acmicpc.net/problem/11060
"""

import sys
input = sys.stdin.readline

n = int(input())
miro = list(map(int, input().split()))
dp = [n+1] * n
dp[0] = 0

for i in range(n):
    # 점프로 갈 수 있는 칸 확인
    for j in range(1, miro[i]+1):
        if i+j < n:

            # 점프한 칸에 점프 횟수에 값을 최솟값으로 초기화
            dp[i+j] = min(dp[i+j], dp[i]+1)

print(dp[n-1] if dp[n-1] != n+1 else -1)