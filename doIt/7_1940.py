"""주몽
https://www.acmicpc.net/problem/1940

투포인터
"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(map(int, input().split()))

a.sort()

s = 0
e = n-1
res = 0

while s < e:
    if a[s] + a[e] < m:
        s += 1
    elif a[s] + a[e] > m:
        e -= 1
    else:
        s += 1
        e -= 1
        res += 1
print(res)