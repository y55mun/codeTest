""" 버블 소트
https://www.acmicpc.net/problem/1377
"""

import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i))

maxx = 0
a = sorted(a)

for i in range(n):
    if maxx < a[i][1] - i:
        maxx = a[i][1] - i

print(maxx+1)