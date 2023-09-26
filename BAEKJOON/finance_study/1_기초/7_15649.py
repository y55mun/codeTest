""" N과 M (1)
https://www.acmicpc.net/problem/15649
"""
import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
list_n = [i for i in range(1, n+1)]

answers = list(permutations(list_n, m))

for i in answers:
    print(' '.join(map(str, i)))