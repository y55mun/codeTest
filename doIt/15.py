""" 수 정렬하기
https://www.acmicpc.net/problem/2750
"""
import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

for i in range(n):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

for i in range(n):
    print(a[i])