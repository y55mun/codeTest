""" 최소, 최대
https://www.acmicpc.net/problem/10818
"""
import sys
input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))
print(min(cases), max(cases))
