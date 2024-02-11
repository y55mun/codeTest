""" 쉬운 계단 수
https://www.acmicpc.net/problem/10844
"""

import sys
input = sys.stdin.readline

n = int(input())
d = [[0 for j in range(11)] for i in range(n+1)]

mod = 1000000000

for i in range(1,10):
    d[1][i] = 1

for i in range(2, n+1):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]

    for j in range(1,9):
        d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % mod

sum = 0
for i in range(10):
    sum = (sum+d[n][i]) % mod

print(sum)

