"""X보다 작은 수
https://www.acmicpc.net/problem/10871
"""

n, x = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

for i in nums:
    if i < x:
        ans.append(i)

print(ans)