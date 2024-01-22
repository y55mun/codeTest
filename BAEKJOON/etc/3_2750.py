""" 수 정렬하기
- 푼 날짜:
https://www.acmicpc.net/problem/2750
"""
n = int(input())

a = [int(input()) for _ in range(n)]

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(*a)