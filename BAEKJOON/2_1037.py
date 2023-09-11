""" 약수
https://www.acmicpc.net/problem/1037
"""

import sys
input = sys.stdin.readline

total = int(input())    # 진짜 약수의 개수
real_div = list(map(int, input().split()))   # 진짜 약수

"""
while True:
    n = max(real_div)
    n은 real_div[i]의 배수 -> real_div[i] % n == 0
    real_div[i] != 1 and real_div[i] != n

"""