""" 이동하기
https://www.acmicpc.net/problem/11048

아이디어
- dp
- dp[i][j]: 그 전에 왼쪽, 위, 왼쪽 위 대각선에서 올 때 가장 큰 값을 넣는다
-
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
candy = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * (m+1)] * (n+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        """
        <top-down 방식 풀이>
        - 차례대로: 위, 왼쪽, 왼쪽 위에서 온 경우를 나타냄
        - dp[i][j] 는 (i, j)까지 왔을때 최대 사탕의 수 이므로 
        각 방향에서 오는 dp와 목적지의 사탕의 개수를 더했을 때의 최대값을 
        다음 dp로 넣는다.
        """
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i-1][j-1]
print(dp[n][m])