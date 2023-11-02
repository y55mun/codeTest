""" A+B - 7
https://www.acmicpc.net/problem/11021
"""

import sys
input = sys.stdin.readline

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
    print("Case #", i+1 ,": ", sum(cases[i]), sep='')
