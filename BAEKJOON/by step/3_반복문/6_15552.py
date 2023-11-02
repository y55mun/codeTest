""" 빠른 A+B
https://www.acmicpc.net/problem/15552
"""
import sys
input = sys.stdin.readline

t = int(input())
cases = [list(map(int, input().split())) for _ in range(t)]

for i in cases:
    print(sum(i))

