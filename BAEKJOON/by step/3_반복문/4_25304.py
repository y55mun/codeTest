""" 영수증
https://www.acmicpc.net/problem/25304
"""

import sys
input = sys.stdin.readline

X = int(input())    # 영수증에 적힌 총 금액
N = int(input())    # 구매한 물건의 종류의 수
product = [list(map(int, input().split())) for _ in range(N)]   # 물건의 가격, 개수

total = 0
for i in range(N):
    total += product[i][0] * product[i][1]

if total == X:
    print("Yes")
else:
    print("No")