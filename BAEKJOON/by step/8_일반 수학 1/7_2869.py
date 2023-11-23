""" 달팽이는 올라가고 싶다
https://www.acmicpc.net/problem/2869
"""
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

days = (v-b) // (a-b)

if days == int(days):
    print(int(days))
else:
    print(int(days) + 1)