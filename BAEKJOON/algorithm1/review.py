""" 퇴사
https://www.acmicpc.net/problem/14501
"""

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+2)
t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())