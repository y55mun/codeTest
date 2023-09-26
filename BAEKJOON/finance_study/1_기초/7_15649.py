""" N과 M (1)
https://www.acmicpc.net/problem/15649
"""
import sys
input = sys.stdin.readline
from itertools import permutations

n, m = list(map(int, input().split()))


print(list(permutations(n,m)))