""" 달팽이는 올라가고 싶다
https://www.acmicpc.net/problem/2869
"""
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
now_distance = 0  # 현재까지의 거리
days = 1  # 올라가는데 걸린 날짜

while now_distance < v:
    now_distance += a

    if now_distance < v:
        now_distance -= b

        days += 1
print(days)