""" 알고리즘 수업 - 점근적 표기 1
https://www.acmicpc.net/problem/24313
"""

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1*n0 + a0 <= c*n0 and c>= a1:
    print(1)
else:
    print(0)