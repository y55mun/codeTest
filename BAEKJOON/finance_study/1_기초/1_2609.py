""" 최대공약수와 최소공배수
https://www.acmicpc.net/problem/2609
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def gcd(n,m):
    if n%m == 0:
        return m
    else:
        return gcd(m, n%m)

print(gcd(n,m))

print((n*m)// gcd(m,n))