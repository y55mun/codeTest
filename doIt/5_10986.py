'''나머지 합
https://www.acmicpc.net/problem/10986
'''

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n # 합 배열
c = [0] * m
answer = 0

s[0] = a[0]
for i in range(1, n):
    s[i] = s[i-1] + a[i]

for i in range(n):
    rem = s[i] % m
    if rem == 0:
        answer += 1
    c[rem] += 1

for i in range(m):
    if c[i] > 1:
        answer += (c[i]*(c[i]-1)//2)

print(answer)