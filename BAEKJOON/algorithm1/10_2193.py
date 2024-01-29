""" 이친수
https://www.acmicpc.net/problem/2193

d[i][j]: 길이 i 인 이친수가 j로 끝나는 개수(경우의 수)
"""

import sys
input = sys.stdin.readline

n = int(input())
d = [[0 for j in range(2)] for i in range(n+1)]
d[1][1] = 1
d[1][0] = 0

for i in range(2, n+1):
    d[i][0] = d[i-1][1] + d[i-1][0]
    d[i][1] = d[i-1][0]

print(d[n][0] + d[n][1])