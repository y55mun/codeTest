""" 이친수
https://www.acmicpc.net/problem/2193
"""

import sys
input = sys.stdin.readline

n = int(input())
d = [[0 for j in range(2)] for i in range(n+1)]
d[1][1] = 1
