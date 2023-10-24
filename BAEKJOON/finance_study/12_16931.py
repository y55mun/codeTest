""" 겉넓이
https://www.acmicpc.net/problem/16931

up, down
left, right
front, back 의 넓이를 구하면 됨!

Q. left, front 의 넓이를 어떻게 구해야 할까
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

up = N*M
