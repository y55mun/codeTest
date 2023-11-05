""" X보다 작은 수
https://www.acmicpc.net/problem/10871
"""

n,x = map(int, input().split())
cases = list(map(int, input().split()))

ans = []

for i in range(n):
    if cases[i] < x:
        ans.append(cases[i])

print(*ans)
