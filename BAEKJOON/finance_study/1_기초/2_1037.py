""" 약수
https://www.acmicpc.net/problem/1037
"""

import sys
input = sys.stdin.readline

total = int(input())    # 진짜 약수의 개수
real_div = list(map(int, input().split()))   # 진짜 약수

real_div.sort()

print(real_div[0] * real_div[-1])